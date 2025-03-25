
-- Create sample tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2)
);

CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    unit_price DECIMAL(10,2)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category_id INT,
    supplier_id INT
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    name VARCHAR(100),
    parent_category_id INT
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);

-- Inefficient query with multiple problems:
-- 1. Unnecessary joins
-- 2. No proper indexing assumed
-- 3. Cartesian product risk
-- 4. No limiting of results
-- 5. Complex calculations in JOIN conditions
SELECT 
    c.name AS customer_name,
    o.order_id,
    p.name AS product_name,
    cat.name AS category_name,
    s.name AS supplier_name,
    oi.quantity * oi.unit_price AS item_total,
    EXTRACT(EPOCH FROM (o.order_date - c.created_at))/86400 AS days_since_customer_creation
FROM customers c
INNER JOIN orders o 
    ON c.customer_id = o.customer_id
INNER JOIN order_items oi 
    ON o.order_id = oi.order_id
INNER JOIN products p 
    ON oi.product_id = p.product_id
INNER JOIN categories cat 
    ON p.category_id = cat.category_id
INNER JOIN suppliers s 
    ON p.supplier_id = s.supplier_id
WHERE 
    o.order_date >= DATEADD(year, -1, CURRENT_TIMESTAMP)
    AND oi.quantity * oi.unit_price > 100
    AND EXISTS (
        SELECT 1 
        FROM categories parent_cat 
        WHERE cat.parent_category_id = parent_cat.category_id
    )
ORDER BY 
    item_total DESC,
    customer_name;

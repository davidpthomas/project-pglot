const { test, expect } = require('@playwright/test');

test.describe('Amazon iPhone 16 Search Tests', () => {
  test('should find at least 10 iPhone 16 results on Amazon', async ({ page }) => {
    // Navigate to Amazon.com
    await page.goto('https://amazon.com');
    
    // Wait for the page to load and search box to be visible
    await page.waitForSelector('#twotabsearchtextbox');
    
    // Search for iPhone 16
    await page.fill('#twotabsearchtextbox', 'iPhone 16');
    await page.click('#nav-search-submit-button');
    
    // Wait for search results to load
    await page.waitForSelector('[data-component-type="s-search-result"]');
    
    // Count the search results
    const searchResults = await page.locator('[data-component-type="s-search-result"]');
    const resultCount = await searchResults.count();
    
    // Verify there are at least 10 results
    expect(resultCount).toBeGreaterThanOrEqual(10);
    
    // Log the actual count for debugging
    console.log(`Found ${resultCount} iPhone 16 search results`);
    
    // Verify the first 10 results contain iPhone-related content
    for (let i = 0; i < Math.min(10, resultCount); i++) {
      const result = searchResults.nth(i);
      const titleElement = result.locator('h2 span').first();
      const title = await titleElement.textContent();
      
      // Verify each result title contains iPhone or related terms
      expect(title.toLowerCase()).toMatch(/iphone|apple/);
      console.log(`Result ${i + 1}: ${title}`);
    }
    
    // Take a screenshot for verification
    await page.screenshot({ path: 'amazon_iphone16_results.png', fullPage: true });
  });
  
  test('should verify exactly 10 iPhone 16 results are displayed per page', async ({ page }) => {
    // Navigate to Amazon.com
    await page.goto('https://amazon.com');
    
    // Search for iPhone 16
    await page.fill('#twotabsearchtextbox', 'iPhone 16');
    await page.click('#nav-search-submit-button');
    
    // Wait for search results to load
    await page.waitForSelector('[data-component-type="s-search-result"]');
    
    // Get the first 10 results specifically
    const searchResults = await page.locator('[data-component-type="s-search-result"]');
    const first10Results = searchResults.first(10);
    const first10Count = await first10Results.count();
    
    // Verify we can find exactly 10 results (or at least 10 if there are more)
    expect(first10Count).toBe(10);
    
    console.log(`Successfully verified ${first10Count} iPhone 16 results are available`);
    
    // Verify each of the 10 results has required elements
    for (let i = 0; i < first10Count; i++) {
      const result = first10Results.nth(i);
      
      // Check that each result has a title
      const titleExists = await result.locator('h2').count() > 0;
      expect(titleExists).toBe(true);
      
      // Check that each result has an image
      const imageExists = await result.locator('img').count() > 0;
      expect(imageExists).toBe(true);
      
      console.log(`Result ${i + 1}: Verified title and image elements exist`);
    }
  });
});
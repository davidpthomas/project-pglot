# Amazon iPhone 16 Playwright Test

This project contains Playwright tests to verify that Amazon.com returns at least 10 search results when searching for "iPhone 16".

## Setup

1. Install Node.js (if not already installed)
2. Install dependencies:
   ```bash
   npm install
   ```

3. Install Playwright browsers:
   ```bash
   npm run install-browsers
   ```

## Running the Tests

### Run all tests (headless mode):
```bash
npm test
```

### Run tests with browser visible:
```bash
npm run test:headed
```

### Run tests in debug mode:
```bash
npm run test:debug
```

### Run specific test file:
```bash
npx playwright test amazon_iphone16_test.js
```

## Test Description

The test suite includes two main test cases:

1. **Basic Search Verification**: 
   - Navigates to Amazon.com
   - Searches for "iPhone 16"
   - Verifies that at least 10 search results are returned
   - Validates that each result contains iPhone or Apple-related content
   - Takes a screenshot for verification

2. **Detailed Result Verification**:
   - Performs the same search
   - Specifically verifies exactly 10 results are available
   - Checks that each result has required elements (title, image)
   - Provides detailed logging of each result

## Test Results

The tests will:
- Generate screenshots in the project directory
- Create HTML reports in the `playwright-report` directory
- Log detailed information about each search result
- Verify both the quantity and quality of search results

## Files

- `amazon_iphone16_test.js` - Main test file
- `playwright.config.js` - Playwright configuration
- `package.json` - Project dependencies and scripts
- `README.md` - This documentation

## Notes

- The test searches for "iPhone 16" on Amazon.com
- Results may vary based on Amazon's current inventory and search algorithm
- The test is designed to be robust and handle variations in search results
- Screenshots are automatically captured for verification purposes
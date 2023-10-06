import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Update the URL and expected title
TEST_URL = "http://www.google.com"
EXPECTED_TITLE = "Google"

@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    # If you need to add options, you can do so here
    
    driver = webdriver.Remote(
        command_executor='http://selenium:4444',
        options=options
    )

    # Yield the driver to the test function
    yield driver

    # Close the browser window
    driver.quit()

def test_google_search(driver):
    """
    Basic test to navigate to the Google page, perform a search, and check the title.
    """
    # Navigate to the test URL
    driver.get(TEST_URL)

    # Check that the title of the page is as expected
    assert EXPECTED_TITLE in driver.title

    # Find the search box using its name attribute value
    search_box = driver.find_element("name", "q")

    # Type 'Python' in the search box
    search_box.send_keys("Python")

    # Press the Enter key
    search_box.send_keys(Keys.RETURN)

    # Check that some results are displayed
    assert "No results found." not in driver.page_source


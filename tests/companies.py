import pytest

from linkedin.spiders.companies import extracts_see_all_url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Your LinkedIn URLs
GOOGLE = "https://www.linkedin.com/company/google"
GOOGLE_USERS_LIST = "https://www.linkedin.com/search/results/people/?facetCurrentCompany=[%221441%22%2C%22621453%22%2C%22791962%22%2C%222374003%22%2C%2216140%22%2C%2210440912%22]"

@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    # If you need to add options, you can do so here
    # For example: options.add_argument('--headless')
    
    driver = webdriver.Remote(
        command_executor='http://selenium:4444',
        options=options
    )

    # Yield the driver to the test function
    yield driver

    # Close the browser window
    driver.quit()

@pytest.mark.skip
def test_extracts_see_all_url(driver):
    driver.get(GOOGLE)
    url = extracts_see_all_url(driver)
    print(url)
    assert url.startswith(
        "https://www.linkedin.com/search/results/people/?facetCurrentCompany="
    )


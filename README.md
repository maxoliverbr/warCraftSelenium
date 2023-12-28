# WarCraft Selenium Project

This project utilizes Selenium, a powerful web testing tool, to automate testing for the WarCraft game's web application. Selenium allows for browser automation and interaction with web elements, enabling the creation of robust automated tests.

## Prerequisites

Before running the tests in this project, make sure you have the following prerequisites installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Chrome](https://www.google.com/chrome/) or [Firefox](https://www.mozilla.org/firefox/) browser
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) or [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (WebDriver for Chrome or Firefox)

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/maxoliverbr/warCraftSelenium.git
    ```

2. Navigate to the project directory:

    ```bash
    cd warCraftSelenium
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the appropriate WebDriver (ChromeDriver or GeckoDriver) and ensure it's in your system's PATH.

## Project Structure

The project follows a standard structure for Selenium projects:

- **tests:** Contains test scripts for different features of the WarCraft application.
- **pages:** Includes Page Object Model (POM) classes representing web pages and their elements.
- **config:** Configuration files for WebDriver setup, environment variables, etc.
- **reports:** Generated test reports after test execution.
- **requirements.txt:** Lists the project dependencies.

## Writing Tests

Write your test scripts in the `tests` directory, utilizing the Selenium WebDriver and the Page Object Model.

Example test script (`tests/login_test.py`):

```python
from selenium import webdriver
from pages.login_page import LoginPage

def test_successful_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    
    login_page.open_login_page()
    login_page.login_with_credentials("valid_username", "valid_password")
    
    assert login_page.is_user_logged_in(), "User login failed"

    driver.quit()

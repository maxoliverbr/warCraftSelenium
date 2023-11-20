import pytest
from selenium import webdriver
from utilities.testdata import TestData

"""
Fixture to open the browser instance for each test case.
"""


@pytest.fixture(params=["chrome"])
#@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-notifications')
        options.add_argument('--no-sandbox')
        options.add_argument('--verbose')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--verbose')
        driver = webdriver.Firefox(options=options)
    elif request.param == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        options.add_argument('--verbose')
        driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    # print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    # print("Close Driver")
    driver.close()

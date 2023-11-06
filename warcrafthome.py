""" Warcraft Selenium+Chrome SignUp automation on Github Actions """
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import logging
from utilities.testdata import TestData
import time


class TestWarCraftSignUp:
    """
    Pytest Test Class
    """

    def setup_class(self):
        """
        faker: Faker Ojbect
        options: Selenium WebDriver options
        driver: Selenium WebDriver
        vars: Selenium vars
        """
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger()
        self.faker = None
        self.options = None
        self.driver = None
        self.vars = None

    def setup_method(self):
        """
        setup helper functions
        :return: None
        """
        self.testdata = TestData()

    def teardown_method(self):
        """
        Teardown helper method
        """
        self.driver.quit()

    @pytest.mark.usefixtures("initialize_driver")
    def test_warcraftsignup(self):
        """
        Warcraft Sign Up test case
        :return: String
        """

        # Test name: WarCraftLogin
        # Step # | name | target | value

        # 1 | open | /en-us/start |
        self.driver.get("https://worldofwarcraft.blizzard.com/en-us/start")

        # 2 | setWindowSize | 1838x1017 |
        self.driver.set_window_size(1920, 1040)

        # 2 | maximizeWindow | set window to max resolution
        # self.driver.maximize_window()

        # 3 | first shadow dom | find first shadow dom
        shadow_root_0 = self.driver.find_element(By.CSS_SELECTOR, ".SiteNav").shadow_root

        # 4 | first second dom | find first second dom
        shadow_root_1 = shadow_root_0.find_element(By.CSS_SELECTOR, "#blz-nav-sign-up").shadow_root

        # 5 | signup | find signup element
        signup = shadow_root_1.find_element(By.ID, "blz-nav-sign-up")

        # 6 | signup | start signup flow
        self.driver.execute_script("arguments[0].click();", signup)

        # 7 | assert | confirm we are on the correct page
        signup_text = self.driver.find_element(By.XPATH,
                                               "//h1[@class='step__title step__block']").text
        # assert signup_text is correct
        assert signup_text == "Sign Up With"

        # 8 | birthdate | enter birthdate mm/dd/yyyy
        self.driver.find_element(By.XPATH,
                                 "//button[@class='step__button step__button--primary']").click()

        error_text = self.driver.find_element(By.XPATH,
                                              "//li[@class='step__field-errors-item']").text

        assert error_text == "Your date of birth is required"

        # 9 | continue | click continue

        self.driver.find_element(By.XPATH, "//*[@name='dob-plain']").click()

        self.driver.find_element(By.XPATH, "//input[@name='dob-month']").send_keys(self.testdata.dob_day)
        self.driver.find_element(By.XPATH, "//input[@name='dob-day']").send_keys(self.testdata.dob_mon)
        self.driver.find_element(By.XPATH, "//input[@name='dob-year']").send_keys(self.testdata.dob_year)

        self.driver.save_screenshot('reports/ss/dob.png')

        self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        self.driver.save_screenshot('reports/ss/continue.png')

        self.driver.find_element(By.ID, "capture-first-name").send_keys(self.testdata.user_first_name)

        self.driver.save_screenshot('reports/ss/firstname.png')

        self.driver.find_element(By.ID, "capture-last-name").send_keys(self.testdata.user_last_name)

        self.driver.save_screenshot('reports/ss/last.png')

        self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        self.driver.find_element(By.ID, "capture-email").send_keys(self.testdata.user_email)

        self.driver.find_element(By.ID, "capture-phone-number").send_keys(self.testdata.user_phone)

        self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        step_name = self.driver.find_element(By.XPATH, "//h1[@class='step__title step__block']").text

        assert step_name == 'Identify Your Account'

        self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        time.sleep(1)

        self.driver.save_screenshot('emailphone.png')

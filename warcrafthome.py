""" Warcraft Selenium+Chrome SignUp automation on Github Actions """
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time
from utilities.testdata import TestData
from pages.base_test import BaseTest
from pages.basepage import BasePage


class TestWarCraftSignUp(BaseTest):
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

    def test_warcraftsignup(self):
        """
        Warcraft Sign Up test case
        :return: String
        """
        page = BasePage(self.driver)

        # Test name: WarCraftLogin
        # Step # | name | target | value

        # 1 | open | /en-us/start |
        page.load(TestData.url)

        # 2 | setWindowSize | 1838x1017 |
        page.set_size(1920, 1080)

        # 3 | first shadow dom | find first shadow dom
        shadow_root_0 = self.driver.find_element(*page.shadow_root_0_css).shadow_root

        # 4 | first second dom | find first second dom
        shadow_root_1 = shadow_root_0.find_element(*page.shadow_root_1_css).shadow_root

        # 5 | signup | find signup element
        signup = shadow_root_1.find_element(*page.signup_id)

        # 6 | signup | start signup flow
        self.driver.execute_script(page.jsclick, signup)

        # 7 | assert | confirm we are on the correct page
        signup_text = self.driver.find_element(*page.signup_text_xpath).text

        # assert signup_text is correct
        assert signup_text == page.signup_text_expected

        # 8 | birthdate | enter birthdate mm/dd/yyyy
        page.click(page.bird_date_xpath)

        error_text = page.get_text(page.error_text_xpath)

        assert error_text == page.error_text_expected

        # 9 | continue | click continue
        page.click(page.dob_xpath)

        page.set(page.dob_month_xpath, TestData.dob_mon)
        page.set(page.dob_day_xpath, TestData.dob_day)
        page.set(page.dob_year_xpath, TestData.dob_year)

        # self.driver.find_element(By.XPATH, "//input[@name='dob-month']").send_keys(self.testdata.dob_mon)
        # self.driver.find_element(By.XPATH, "//input[@name='dob-day']").send_keys(self.testdata.dob_day)
        # self.driver.find_element(By.XPATH, "//input[@name='dob-year']").send_keys(self.testdata.dob_year)

        # self.driver.save_screenshot('reports/ss/dob.png')

        page.click(page.continue_id)

        page.save_screenshot('reports/ss/continue.png')

        page.set(page.first_name_id, TestData.user_first_name)

        # self.driver.find_element(By.ID, "capture-first-name").send_keys(self.testdata.user_first_name)

        page.save_screenshot('reports/ss/firstname.png')

        page.set(page.last_name_id)
        # self.driver.find_element(By.ID, "capture-last-name").send_keys(self.testdata.user_last_name)

        page.save_screenshot('reports/ss/last.png')

        page.click(page.continue_id)
        # self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        page.set(page.email_id)
        # self.driver.find_element(By.ID, "capture-email").send_keys(self.testdata.user_email)

        page.set(page.phone_id, TestData.user_phone)
        # self.driver.find_element(By.ID, "capture-phone-number").send_keys(self.testdata.user_phone)

        page.click(page.continue_id)
        # self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        step_name = page.get_text(step_name_xpath)
        # step_name = self.driver.find_element(By.XPATH, "//h1[@class='step__title step__block']").text

        assert step_name == page.step_name_expect

        page.click(page.continue_id)
        #self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        time.sleep(1)

        page.save_screenshot('reports/ss/'emailphone.png')


""" Warcraft Selenium+Chrome SignUp automation on Github Actions """
import logging
import time

import pytest

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

    # Firefox fails on 2560 and 1366
    # @pytest.mark.parametrize("width,height", [(1920, 1080), (2560, 1080), (1366, 768)])
    @pytest.mark.parametrize("width,height", [(1920, 1080)])
    def test_warcraftsignup(self, width, height):
        """
        Warcraft Sign Up test case
        Using different screensizes
        :return: String
        """
        page = BasePage(self.driver)

        # Test name: WarCraftLogin
        # Step # | name | target | value

        # 1 | open | /en-us/start |
        page.load(TestData.url)

        # 2 | setWindowSize | 1838x1017 |
        page.set_size(width, height)

        # 3 | first shadow dom | find first shadow dom
        shadow_root_0 = page.get_shadow(page.shadow_root_0_css)

        # 4 | first second dom | find first second dom
        shadow_root_1 = page.get_nested_shadow(shadow_root_0, page.shadow_root_1_css)

        # 5 | signup | find signup element
        signup = shadow_root_1.find_element(*page.signup_id)

        # 6 | signup | start signup flow
        self.driver.execute_script(page.jsclick, signup)

        # 7 | assert | confirm we are on the correct page
        signup_text = self.driver.find_element(*page.signup_text_xpath).text

        # assert signup_text is correct
        assert signup_text == page.signup_text_expected

        # 8 | birthdate | click continue without birthdate
        page.click(page.bird_date_xpath)

        error_text = page.get_text(page.error_text_xpath)

        # assert error message is correct
        assert error_text == page.error_text_expected
        page.click(page.dob_xpath)

        # 9 | birthdate | enter birthdate mm/dd/yyyy
        page.set(page.dob_month_xpath, TestData.dob_mon)
        page.set(page.dob_day_xpath, TestData.dob_day)
        page.set(page.dob_year_xpath, TestData.dob_year)

        # 10 | continue | click continue
        page.click(page.continue_id)
        page.save_screenshot('reports/ss/continue.png')

        # 11 | user info | enter first & last name
        page.set(page.first_name_id, TestData.user_first_name)
        page.set(page.last_name_id, TestData.user_last_name)
        page.save_screenshot('reports/ss/last.png')

        page.click(page.continue_id)

        # 12 | user info part 2 | enter email and phone
        page.set(page.email_id, TestData.user_email)
        page.set(page.phone_id, TestData.user_phone)

        page.click(page.continue_id)

        # 13 | assert step name
        step_name = page.get_text(page.step_name_xpath)

        assert step_name == page.step_name_expect

        page.click(page.continue_id)

        # wait page load
        time.sleep(1)
        page.save_screenshot('reports/ss/emailphone.png')

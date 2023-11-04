import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# import Faker from Faker


class TestWarCraftSignUp():
    def setup_method(self, method):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_warCraftLogin(self):
        # Test name: WarCraftLogin
        # Step # | name | target | value

        # 1 | open | /en-us/start |
        self.driver.get("https://worldofwarcraft.blizzard.com/en-us/start")

        # 2 | setWindowSize | 1838x1017 |
        self.driver.set_window_size(1920, 1040)

        # 2 | maximizeWindow | set window to max resolution
        # self.driver.maximize_window()

        # 3 | implicit wait | add implicit wait due to long load times
        self.driver.implicitly_wait(10)

        # 4 | first shadow dom | find first shadow dom
        shadow_root_0 = self.driver.find_element(By.CSS_SELECTOR, ".SiteNav").shadow_root

        # 5 | first second dom | find first second dom
        shadow_root_1 = shadow_root_0.find_element(By.CSS_SELECTOR, "#blz-nav-sign-up").shadow_root

        # 6 | signup | find signup element
        signup = shadow_root_1.find_element(By.ID, "blz-nav-sign-up")

        # 7 | signup | start signup flow
        self.driver.execute_script("arguments[0].click();", signup)

        # 8 | assert | confirm we are on the correct page
        signup_text = self.driver.find_element(By.XPATH, "//h1[@class='step__title step__block']").text

        assert signup_text == "Sign Up With"

        # 9 | birthdate | enter birthdate mm/dd/yyyy
        self.driver.find_element(By.XPATH, "//button[@class='step__button step__button--primary']").click()

        error_text = self.driver.find_element(By.XPATH, "//li[@class='step__field-errors-item']").text

        assert error_text == "Your date of birth is required"

        # 10 | continue | click continue

        # wait before close browser
        time.sleep(2)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestWarCraftLogin():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_warCraftLogin(self):
        # Test name: WarCraftLogin
        # Step # | name | target | value
        # 1 | open | /en-us/start |
        self.driver.get("https://worldofwarcraft.blizzard.com/en-us/start")
        # 2 | setWindowSize | 1838x1017 |
        self.driver.set_window_size(1838, 1017)
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

        # wait before close browser
        time.sleep(2)

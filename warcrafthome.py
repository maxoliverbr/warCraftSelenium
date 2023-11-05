""" Warcraft Selenium+Chrome SignUp automation on Github Actions """
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker


@pytest.fixture(params=['chrome', 'firefox'])
class TestWarCraftSignUp:
    """
    Pytest Test Class
    """
    def __init__(self):
        """
        faker: Faker Ojbect
        options: Selenium WebDriver options
        driver: Selenium WebDriver
        vars: Selenium vars
        """
        self.faker = None
        self.options = None
        self.driver = None
        self.vars = None

    def setup_method(self):
        """
        setup helper functions
        :return: None
        """
        self.faker = Faker(['pt_BR'])
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument("--disable-notifications")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--verbose')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-software-rasterizer')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.implicitly_wait(10)
        self.vars = {}

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

        assert signup_text == "Sign Up With"

        # 8 | birthdate | enter birthdate mm/dd/yyyy
        self.driver.find_element(By.XPATH,
                                 "//button[@class='step__button step__button--primary']").click()

        error_text = self.driver.find_element(By.XPATH,
                                              "//li[@class='step__field-errors-item']").text

        assert error_text == "Your date of birth is required"

        # 9 | continue | click continue

        self.driver.find_element(By.XPATH, "//*[@name='dob-plain']").click()

        self.driver.find_element(By.XPATH, "//input[@name='dob-month']").send_keys('01')
        self.driver.find_element(By.XPATH, "//input[@name='dob-day']").send_keys('01')
        self.driver.find_element(By.XPATH, "//input[@name='dob-year']").send_keys('1970')

        self.driver.save_screenshot('reports/ss/dob.png')

        self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        self.driver.save_screenshot('reports/ss/continue.png')

        self.driver.find_element(By.ID, "capture-first-name").send_keys(self.faker.first_name())

        self.driver.save_screenshot('reports/ss/firstname.png')

        self.driver.find_element(By.ID, "capture-last-name").send_keys(self.faker.last_name())

        self.driver.save_screenshot('reports/ss/last.png')

        self.driver.find_element(By.ID, "flow-form-submit-btn").click()

        self.driver.find_element(By.ID, "capture-email").send_keys(self.faker.email())

        self.driver.find_element(By.ID, "capture-phone-number").send_keys(self.faker.phone_number())

        self.driver.save_screenshot('reports/ss/emailphone.png')

""" POM BasePage """
from selenium.webdriver.common.by import By


class BasePage:
    """
    BasePage contains methods common to all Page Objects
    """
    shadow_root_0_css = (By.CSS_SELECTOR, ".SiteNav")
    shadow_root_1_css = (By.CSS_SELECTOR, "#blz-nav-sign-up")
    signup_id = (By.ID, "blz-nav-sign-up")
    jsclick = "arguments[0].click();"

    signup_text_xpath = (By.XPATH, "//h1[@class='step__title step__block']")
    signup_text_expected = "Sign Up With"

    bird_date_xpath = (By.XPATH, "//button[@class='step__button step__button--primary']")

    error_text_xpath = By.XPATH, "//li[@class='step__field-errors-item']"
    error_text_expected = "Your date of birth is required"

    dob_xpath = By.XPATH, "//*[@name='dob-plain']"

    dob_month_xpath = By.XPATH, "//input[@name='dob-month']"

    continue_id = By.ID, "flow-form-submit-btn"

    first_name_id = By.ID, "capture-first-name"
    last_name_id = By.ID, "capture-last-name"

    email_id = By.ID, "capture-email"
    phone_id = By.ID, "capture-phone-number"
    step_name_xpath = By.XPATH, "//h1[@class='step__title step__block']"
    step_name_expect = 'Identify Your Account'
    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def set_size(self, x, y):
        self.driver.set_window_size(x, y)

    def get_shadow(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector).shadow_root

    def get_nested_shadow(self, dom, selector):
        return dom.find_element(By.CSS_SELECTOR, selector).shadow_root

    def save_screenshot(self, path):
        self.driver.save_screenshot(path)

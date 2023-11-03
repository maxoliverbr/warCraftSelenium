class BasePage:
    """
    BasePage contains methods common to all Page Objects
    """

    def __init__(self, driver):
        self.driver = driver

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

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_windows(self):
        return self.driver.window_handles

    def set_window(self, window):
        return self.driver.switch_to.window(window)


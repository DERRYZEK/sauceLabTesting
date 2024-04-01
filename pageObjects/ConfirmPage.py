from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.CSS_SELECTOR, "#first-name")
    last_name = (By.CSS_SELECTOR, "#last-name")
    zipcode = (By.XPATH, "//input[@id='postal-code']")
    continue_button =(By.CSS_SELECTOR,"#continue")
    finish_button = (By.CSS_SELECTOR, "#finish")
    success_message =(By.CSS_SELECTOR,".complete-header")

    def get_first_name(self):
        return self.driver.find_element(*ConfirmPage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*ConfirmPage.last_name)

    def get_zipcode(self):
        return self.driver.find_element(*ConfirmPage.zipcode)

    def get_continue_button(self):
        return self.driver.find_element(*ConfirmPage.continue_button)

    def get_finish_button(self):
        return self.driver.find_element(*ConfirmPage.finish_button)

    def get_success_message(self):
        return self.driver.find_element(*ConfirmPage.success_message)

from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage



class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkout_button = (By.CSS_SELECTOR, "#checkout")
    continue_shopping_button = (By.CSS_SELECTOR, "#continue-shopping")

    def get_checkout_button(self):
        self.driver.find_element(*CheckOutPage.checkout_button).click()
        return ConfirmPage(self.driver)

    def get_continue_shopping_button(self):
        pass

from selenium.webdriver.common.by import By

from pageObjects.ProductsPage import ProductsPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.CSS_SELECTOR, "#user-name")
    password = (By.XPATH, "//input[@id='password']")
    login_button = (By.CSS_SELECTOR, "[id='login-button']")

    def get_user_name(self):
        return self.driver.find_element(*LoginPage.user_name)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        self.driver.find_element(*LoginPage.login_button).click()
        return ProductsPage(self.driver)

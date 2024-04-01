from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    products_names = (By.XPATH, "//div[@class='inventory_item_name']")
    add_to_cart_buttons = (By.XPATH, "//button[text()='Add to cart']")
    cart_button = (By.CSS_SELECTOR, ".shopping_cart_link")

    def get_products_names(self):
        return self.driver.find_elements(*ProductsPage.products_names)

    def get_add_to_cart_buttons(self):
        return self.driver.find_elements(*ProductsPage.add_to_cart_buttons)

    def get_cart_button(self):
        self.driver.find_element(*ProductsPage.cart_button).click()
        return CheckOutPage(self.driver)

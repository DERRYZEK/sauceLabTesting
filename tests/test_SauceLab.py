from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestSauceLab(BaseClass):
    def test_sauce_lab(self, get_user_credentials, get_products,get_confirm_page_data):
        log = self.getLogger()

        login_page = LoginPage(self.driver)

        log.info("Entering username")
        login_page.get_user_name().send_keys(get_user_credentials["username"])

        log.info("Entering password")
        login_page.get_password().send_keys(get_user_credentials["password"])

        products_page = login_page.get_login_button()

        products = products_page.get_products_names()
        i = -1

        for product in products:
            i = i + 1
            log.info("product name")
            product_name = product.text

            if product_name in get_products:
                log.info("clicking on add to cart button")
                products_page.get_add_to_cart_buttons()[i].click()

        check_out_page = products_page.get_cart_button()

        confirm_page = check_out_page.get_checkout_button()

        log.info("entering first name")
        confirm_page.get_first_name().send_keys(get_confirm_page_data["firstname"])

        log.info("Entering last name")
        confirm_page.get_last_name().send_keys(get_confirm_page_data["lastname"])

        log.info("Entering zipcode")
        confirm_page.get_zipcode().send_keys(get_confirm_page_data["zipcode"])

        confirm_page.get_continue_button().click()

        confirm_page.get_finish_button().click()

        success_message = confirm_page.get_success_message().text

        text = "Thank you for your order!"

        assert text == success_message

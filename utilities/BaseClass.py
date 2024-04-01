import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from TestData.ConfirmPageData import ConfirmPageData
from TestData.LoginPageData import LoginPageData
from TestData.ProductPageData import ProductPageData


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        selector = Select(locator)
        selector.select_by_visible_text(text)

    @pytest.fixture(params=LoginPageData.test_LoginPage_Data)
    def get_user_credentials(self, request):
        return request.param

    @pytest.fixture(params=ProductPageData.product_page_data)
    def get_products(self, request):
        return request.param

    @pytest.fixture(params=ConfirmPageData.confirm_page_data)
    def get_confirm_page_data(self, request):
        return request.param

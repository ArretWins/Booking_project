import time

from selenium.common import NoSuchElementException, TimeoutException

from helpers import BASE_URL
from pages.base_page import BasePage
# from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainLocators
import allure


class MainPage(BasePage, MainLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open main page')
    def open(self):
        self.open_page(BASE_URL)

    @allure.step('Assert that main page is opened')
    def assert_main_page_is_opened(self):
        # time.sleep(10)
        self.get_element(self.HEADER_LOGO)
        self.get_element(self.SIGN_UP_BUTTON)
        self.get_element(self.SIGN_IN_BUTTON)
        self.get_element(self.CURRENCY_BUTTON)
        self.get_element(self.LANGUAGE_BUTTON)

    @allure.title('Open register page')
    def open_register_page(self):
        self.click(self.SIGN_UP_BUTTON)

    @allure.title('Open sing in page')
    def open_register_page(self):
        self.click(self.SIGN_IN_BUTTON)


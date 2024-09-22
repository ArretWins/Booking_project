import time

from selenium.common import NoSuchElementException, ElementClickInterceptedException, TimeoutException

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
        # time.sleep(15)
        # self.get_element(self.DECLINE_COOKIES_BUTTON)
        self.click(self.DECLINE_COOKIES_BUTTON)

    @allure.title('Open register page')
    def open_register_page(self):
        self.click(self.SIGN_UP_BUTTON)

    @allure.step('Click to currency button')
    def click_currency_button(self):
        self.click(self.CURRENCY_BUTTON)

    @allure.step('Click to dismiss button')
    def click_dismiss_button(self):
        self.click(self.DISMISS_BUTTON)

    @allure.step('Change currency')
    def change_currency(self, currency):
        if currency == 'CZK':
            self.click(self.CZK_CURRENCY)
            try:
                self.click_dismiss_button()
            except (ElementClickInterceptedException, TimeoutException):
                print("Element click intercepted(didn't find dismiss element)")
        elif currency == 'EUR':
            self.click(self.EUR_CURRENCY)
            try:
                self.click_dismiss_button()
            except (ElementClickInterceptedException, TimeoutException):
                print("Element click intercepted(didn't find dismiss element)")

    @allure.step('Assert that main page is opened')
    def assert_main_page_is_opened(self):
        self.get_element(self.HEADER_LOGO)
        self.get_element(self.SIGN_UP_BUTTON)
        self.get_element(self.SIGN_IN_BUTTON)
        self.get_element(self.CURRENCY_BUTTON)
        self.get_element(self.LANGUAGE_BUTTON)

    @allure.step('Assert that currency is changed')
    def assert_change_of_currency(self, currency):
        if currency == 'CZK':
            self.get_element(self.MAIN_PAGE_CZK_CURRENCY)
        elif currency == 'EUR':
            self.get_element(self.MAIN_PAGE_EUR_CURRENCY)




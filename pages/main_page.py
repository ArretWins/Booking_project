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
        self.add_cookies('ALWCS', '0')
        self.add_cookies('CBARIH', '1')
        self.driver.refresh()

    @allure.step('Assert that main page is opened')
    def assert_main_page_is_opened(self):
        self.get_element(self.HEADER_LOGO)


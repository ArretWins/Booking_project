import time

from selenium.common import NoSuchElementException, TimeoutException

from pages.base_page import BasePage
from locators.register_page_locators import RegisterLocators
import allure


class RegisterPage(BasePage, RegisterLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Click to continue button')
    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    @allure.step('Assert that register page is opened')
    def assert_register_page_is_opened(self):
        self.get_element(self.EMAIL_INPUT)
        self.get_element(self.CONTINUE_BUTTON)

    @allure.step('Assert that alert message is displayed')
    def assert_alert_message(self):
        self.get_element(self.ALERT_DIV)

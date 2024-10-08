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
    def click_continue_button(self, page='email'):
        if page == 'email':
            self.click(self.CONTINUE_BUTTON)
        elif page == 'password':
            self.get_element(self.PASSWORD_INPUT)
            self.click(self.CONTINUE_BUTTON)

    @allure.step('Click to social login')
    def click_social_login(self, social):
        if social == 'Facebook':
            self.click(self.FACEBOOK_LOGIN_BUTTON)
            time.sleep(2)
        elif social == 'Google':
            self.click(self.GOOGLE_LOGIN_BUTTON)
            time.sleep(2)
        elif social == 'Apple':
            self.click(self.APPLE_LOGIN_BUTTON)
            time.sleep(2)

    @allure.step('Input email to register')
    def input_email_to_register(self):
        self.fill(self.EMAIL_INPUT, 'testbookingemail@gmail.com')

    @allure.step('Input password to register')
    def input_password_to_register(self):
        self.fill(self.PASSWORD_INPUT, '1')

    @allure.step('Input confirm password to register')
    def input_confirm_password_to_register(self):
        self.fill(self.PASSWORD_CONFIRM_INPUT, '1')

    @allure.step('Input long confirm password to register')
    def input_long_confirm_password_to_register(self):
        self.fill(self.PASSWORD_CONFIRM_INPUT, '123456789aA')

    @allure.step('Assert that register page is opened')
    def assert_register_page_is_opened(self):
        self.get_element(self.EMAIL_INPUT)
        self.get_element(self.CONTINUE_BUTTON)
        self.get_element(self.FACEBOOK_LOGIN_BUTTON)
        self.get_element(self.GOOGLE_LOGIN_BUTTON)
        self.get_element(self.APPLE_LOGIN_BUTTON)

    @allure.step('Assert that alert message is displayed')
    def assert_alert_message(self, page):
        if page == 'email':
            self.get_element(self.USERNAME_ALERT_DIV)
        elif page == 'password':
            self.get_element(self.PASSWORD_ALERT_DIV)
        elif page == 'short':
            self.get_element(self.SHORT_PASSWORD_ALERT_DIV)
        elif page == 'match':
            self.get_element(self.MATCH_PASSWORD_ALERT_DIV)

    @allure.step('Assert that password page is opened')
    def assert_password_page_is_opened(self):
        self.get_element(self.PASSWORD_INPUT)
        self.get_element(self.PASSWORD_CONFIRM_INPUT)
        self.get_element(self.CONTINUE_BUTTON)

    @allure.step('Assert that social login page is opened')
    def assert_that_social_login_page_is_opened(self, social):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(1)
        if social == 'Facebook':
            self.get_element(self.FACEBOOK_LOGO)
        elif social == 'Google':
            self.get_element(self.GOOGLE_INPUT)
        elif social == 'Apple':
            self.get_element(self.APPLE_INPUT)

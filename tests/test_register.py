import time

import allure

from pages.main_page import MainPage
from pages.register_page import RegisterPage


@allure.feature('Register page')
class TestRegister:

    @allure.title('Open register page')
    def test_open_register(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.assert_register_page_is_opened()

    @allure.title('Assert alert message on email page')
    def test_email_assert_message(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.click_continue_button()
        register_page.assert_alert_message('email')

    @allure.title('Assert that password page is opened')
    def test_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.input_email_to_register()
        register_page.click_continue_button()
        register_page.assert_password_page_is_opened()

    @allure.title('Assert alert message on password page')
    def test_password_assert_message(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.input_email_to_register()
        register_page.click_continue_button()
        register_page.click_continue_button('password')
        register_page.assert_alert_message('password')

    @allure.title('Assert short password alert message')
    def test_short_password_assert_message(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.input_email_to_register()
        register_page.click_continue_button()
        register_page.input_password_to_register()
        register_page.input_confirm_password_to_register()
        register_page.click_continue_button('password')
        register_page.assert_alert_message('short')

    @allure.title('Assert different passwords alert message')
    def test_different_password_assert_message(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.input_email_to_register()
        register_page.click_continue_button()
        register_page.input_password_to_register()
        register_page.input_long_confirm_password_to_register()
        register_page.click_continue_button('password')
        register_page.assert_alert_message('match')

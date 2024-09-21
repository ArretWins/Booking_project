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

    @allure.title('Assert alert message')
    def test_assert_message(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.open_register_page()

        register_page = RegisterPage(driver)
        register_page.click_continue_button()
        register_page.assert_alert_message()


import time

import allure

from pages.main_page import MainPage


@allure.feature('Main page')
class TestMain:

    @allure.title('Open main page')
    def test_open_website(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_main_page_is_opened()

    @allure.title('Change currency to CZK')
    def test_of_change_currency_to_czk(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_currency_button()
        main_page.change_currency('CZK')
        main_page.assert_change_of_currency('CZK')

    @allure.title('Change currency from CZK to EUR')
    def test_of_change_currency_to_eur(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_currency_button()
        main_page.change_currency('CZK')
        main_page.click_currency_button()
        main_page.change_currency('EUR')
        main_page.assert_change_of_currency('EUR')

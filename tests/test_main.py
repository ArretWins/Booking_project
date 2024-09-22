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

    @allure.title('Change language to DEUTSCH')
    def test_of_change_language_to_deutsch(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_language_button()
        main_page.change_language('DEU')
        driver.refresh()
        main_page.assert_change_of_language('DEU')

    @allure.title('Change language from DEUTSCH to ENGLISH')
    def test_of_change_language_to_english(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_language_button()
        main_page.change_language('DEU')
        driver.refresh()
        main_page.click_dismiss_button('DEU')
        main_page.click_language_button()
        main_page.change_language('ENG')
        driver.refresh()
        main_page.assert_change_of_language('ENG')

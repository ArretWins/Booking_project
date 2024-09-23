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
        self.click(self.DECLINE_COOKIES_BUTTON)

    @allure.title('Open register page')
    def open_register_page(self):
        self.click(self.SIGN_UP_BUTTON)

    @allure.step('Click to currency button')
    def click_currency_button(self):
        self.click(self.CURRENCY_BUTTON)

    @allure.step('Click to language button')
    def click_language_button(self):
        self.click(self.LANGUAGE_BUTTON)

    @allure.step('Click to flights button')
    def click_flights(self):
        self.click(self.FLIGHTS)

    @allure.step('Click to dismiss button')
    def click_dismiss_button(self, language='ENG'):
        if language == 'ENG':
            self.click(self.DISMISS_BUTTON)
        elif language == 'DEU':
            self.click(self.DEU_DISMISS_BUTTON)

    @allure.step('Change_language')
    def change_language(self, language):
        if language == 'DEU':
            self.click(self.DEUTSCH_BUTTON)
        elif language == 'ENG':
            self.click(self.ENGLISH_BUTTON)

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

    @allure.step('Search place')
    def search_place(self):
        self.fill(self.PLACE_SEARCH_INPUT, 'Bratislava')
        try:
            self.click_dismiss_button()
        except (ElementClickInterceptedException, TimeoutException):
            print("Element click intercepted(didn't find dismiss element)")

    @allure.step('Choose time')
    def choose_time(self):
        self.click(self.DATES_SEARCH_INPUT)
        self.click(self.FLEXIBLE_DATES_BUTTON)
        self.click(self.WEEKENDS_BUTTON, True)
        self.click(self.SEPTEMBER_BUTTON)
        self.click(self.CHOOSE_TIME_BUTTON)

    @allure.step('Choose occupancy')
    def choose_occupancy(self):
        self.click(self.OCCUPANCY_INPUT)
        self.click(self.PLUS_BUTTON)
        self.click(self.OCCUPANCY_BUTTON)

    @allure.step('Click search button')
    def click_search_button(self):
        self.click(self.SEARCH_PLACE_BUTTON)

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

    @allure.step('Assert that language is changed')
    def assert_change_of_language(self, language):
        if language == 'DEU':
            self.get_element(self.DEUTSCH_TEXT_SPAN)
        elif language == 'ENG':
            self.get_element(self.ENGLISH_TEXT_SPAN)

    @allure.step('Assert that place search works')
    def assert_place_search(self):
        self.get_element(self.PLACE_CONTAINER)

    @allure.step('Assert void place search alert')
    def assert_void_search_alert(self):
        self.get_element(self.SEARCHBOX_ALERT)

    @allure.step('Assert redirect to another page')
    def assert_redirect(self, page):
        if page == 'flights':
            self.get_element(self.GO_TO_GATE_LOGO)

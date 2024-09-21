import allure

from pages.main_page import MainPage


@allure.feature('Main page')
class TestMain:

    @allure.title('Open main page')
    def test_open_website(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_main_page_is_opened()

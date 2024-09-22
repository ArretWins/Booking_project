from selenium.webdriver.common.by import By


class MainLocators:
    HEADER_LOGO = (By.XPATH, '//a[@data-testid="header-booking-logo"]')
    SIGN_UP_BUTTON = (By.XPATH, '//a[@data-testid="header-sign-up-button"]')
    SIGN_IN_BUTTON = (By.XPATH, '//a[@data-testid="header-sign-in-button"]')
    DECLINE_COOKIES_BUTTON = (By.XPATH, '//button[@id="onetrust-reject-all-handler"]')
    DISMISS_BUTTON = (By.XPATH, '//button[@aria-label="Dismiss sign-in info."]')

    CURRENCY_BUTTON = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
    CZK_CURRENCY = (By.XPATH, '//div[text()="CZK"]')
    MAIN_PAGE_CZK_CURRENCY = (By.XPATH, '//span[text()="CZK"]')
    EUR_CURRENCY = (By.XPATH, '//div[text()="EUR"]')
    MAIN_PAGE_EUR_CURRENCY = (By.XPATH, '//span[text()="EUR"]')

    LANGUAGE_BUTTON = (By.XPATH, '//button[@data-testid="header-language-picker-trigger"]')
    ENGLISH_BUTTON = (By.XPATH, '//span[text()="English (UK)"]')
    DEUTSCH_BUTTON = (By.XPATH, '//span[text()="Deutsch"]')


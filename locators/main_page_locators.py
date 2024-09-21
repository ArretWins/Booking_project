from selenium.webdriver.common.by import By


class MainLocators:
    HEADER_LOGO = (By.XPATH, '//a[@data-testid="header-booking-logo"]')
    SIGN_UP_BUTTON = (By.XPATH, '//a[@data-testid="header-sign-up-button"]')
    SIGN_IN_BUTTON = (By.XPATH, '//a[@data-testid="header-sign-in-button"]')
    CURRENCY_BUTTON = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
    LANGUAGE_BUTTON = (By.XPATH, '//button[@data-testid="header-language-picker-trigger"]')

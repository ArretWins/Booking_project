from selenium.webdriver.common.by import By


class MainLocators:
    HEADER_LOGO = (By.XPATH, '//a[@data-testid="header-booking-logo"]')
    PROFILE_BUTTON = (By.XPATH, '//button[@data-testid="header-profile"]')
    CURRENCY_BUTTON = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
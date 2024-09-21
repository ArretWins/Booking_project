from selenium.webdriver.common.by import By


class RegisterLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@type="email"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ALERT_DIV = (By.XPATH, '//div[@id="username-note"]')

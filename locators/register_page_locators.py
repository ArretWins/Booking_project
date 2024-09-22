from selenium.webdriver.common.by import By


class RegisterLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@type="email"]')
    CONTINUE_BUTTON = (By.XPATH, '//button[@type="submit"]')
    USERNAME_ALERT_DIV = (By.XPATH, '//div[@id="username-note"]')
    PASSWORD_ALERT_DIV = (By.XPATH, '//div[@id="confirmed_password-note"]')
    SHORT_PASSWORD_ALERT_DIV = (By.XPATH, '//div[contains(text(), "10 characters")]')
    MATCH_PASSWORD_ALERT_DIV = (By.XPATH, '//div[contains(text(), "match")]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="new_password"]')
    SHOW_PASSWORD_INPUT = (By.XPATH, '//button[@aria-controls="new_password"]')
    SHOW_CONFIRM_INPUT = (By.XPATH, '//button[@aria-controls="confirmed_password"]')
    PASSWORD_CONFIRM_INPUT = (By.XPATH, '//input[@name="confirmed_password"]')

    CONFIRM_EMAIL_BUTTON = (By.XPATH, '//button[@type="submit"]')

    FACEBOOK_LOGIN_BUTTON = (By.XPATH, '//a[contains(@class, "access-panel__social-button-facebook")]')
    FACEBOOK_LOGO = (By.XPATH, '//a[@href="https://www.facebook.com/"]')

    GOOGLE_LOGIN_BUTTON = (By.XPATH, '//a[contains(@class, "access-panel__social-button-google")]')
    GOOGLE_INPUT = (By.XPATH, '//input[@id="identifierId"]')

    APPLE_LOGIN_BUTTON = (By.XPATH, '//a[contains(@class, "access-panel__social-button-apple")]')
    APPLE_INPUT = (By.XPATH, '//input[@id="account_name_text_field"]')



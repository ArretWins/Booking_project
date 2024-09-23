from selenium.webdriver.common.by import By


class MainLocators:
    HEADER_LOGO = (By.XPATH, '//a[@data-testid="header-booking-logo"]')
    SIGN_UP_BUTTON = (By.XPATH, '//a[@data-testid="header-sign-up-button"]')
    SIGN_IN_BUTTON = (By.XPATH, '//a[@data-testid="header-sign-in-button"]')
    FLIGHTS = (By.XPATH, '//a[@id="flights"]')
    GO_TO_GATE_LOGO = (By.XPATH, '//header[@class="css-17vgg1c"]')
    FLIGHTS_PLUS_HOTELS = (By.XPATH, '//a[@id="packages"]')

    DECLINE_COOKIES_BUTTON = (By.XPATH, '//button[@id="onetrust-reject-all-handler"]')
    DISMISS_BUTTON = (By.XPATH, '//button[@aria-label="Dismiss sign-in info."]')
    DEU_DISMISS_BUTTON = (By.XPATH, '//button[@aria-label="Informationen zur Anmeldung ausblenden."]')

    CURRENCY_BUTTON = (By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
    CZK_CURRENCY = (By.XPATH, '//div[text()="CZK"]')
    MAIN_PAGE_CZK_CURRENCY = (By.XPATH, '//span[text()="CZK"]')
    EUR_CURRENCY = (By.XPATH, '//div[text()="EUR"]')
    MAIN_PAGE_EUR_CURRENCY = (By.XPATH, '//span[text()="EUR"]')

    LANGUAGE_BUTTON = (By.XPATH, '//button[@data-testid="header-language-picker-trigger"]')
    ENGLISH_BUTTON = (By.XPATH, '//span[text()="English (UK)"]')
    DEUTSCH_BUTTON = (By.XPATH, '//span[text()="Deutsch"]')
    ENGLISH_TEXT_SPAN = (By.XPATH, '//span[text()="List your property"]')
    DEUTSCH_TEXT_SPAN = (By.XPATH, '//span[text()="Ihre Unterkunft anmelden"]')

    PLACE_SEARCH_INPUT = (By.XPATH, '//input[@id=":rh:"]')
    DATES_SEARCH_INPUT = (By.XPATH, '//div[@data-testid="searchbox-dates-container"]')
    FLEXIBLE_DATES_BUTTON = (By.XPATH, '//button[@aria-controls="flexible-searchboxdatepicker"]')
    WEEKENDS_BUTTON = (By.XPATH, '//span[@class="c907c67d20"]')
    SEPTEMBER_BUTTON = (By.XPATH, '//span[@class="cac967781c"]')
    CHOOSE_TIME_BUTTON = (By.XPATH, '//button[contains(@class, "c994bb94f3")]')

    OCCUPANCY_INPUT = (By.XPATH, '//button[@data-testid="occupancy-config"]')
    PLUS_BUTTON = (By.XPATH, '//button[contains(@class, "f4d78af12a")]')
    OCCUPANCY_BUTTON = (By.XPATH, '//button[contains(@class, "c213355c26 b9fd3c6b3c")]')

    SEARCH_PLACE_BUTTON = (By.XPATH, '//button[contains(@class, "cceeb8986b b9fd3c6b3c")]')
    SEARCHBOX_ALERT = (By.XPATH, '//div[@data-testid="searchbox-alert"]')
    PLACE_CONTAINER = (By.XPATH, '//div[contains(@class, "c82435a4b8 a178069f51")]')


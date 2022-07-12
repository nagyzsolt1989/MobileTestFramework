from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class CreateAlertPage(BasePage):
    """
        Create Alert page locators
    """
    buttonBack = (MobileBy.ACCESSIBILITY_ID, "Alerts")
    titleEditWatchlist = (MobileBy.ACCESSIBILITY_ID, "Create Alert")
    pairBTCUSD = (MobileBy.ACCESSIBILITY_ID, "BTC/USD")
    pairBTCEUR = (MobileBy.ACCESSIBILITY_ID, "BTC/EUR")
    pairBTCGBP = (MobileBy.ACCESSIBILITY_ID, "BTC/GBP")
    pairBTCCHF = (MobileBy.ACCESSIBILITY_ID, "BTC/CHF")
    pairETHUSD = (MobileBy.ACCESSIBILITY_ID, "ETH/USD")
    pairETHEUR = (MobileBy.ACCESSIBILITY_ID, "ETH/EUR")
    pairETHGBP = (MobileBy.ACCESSIBILITY_ID, "ETH/GBP")
    pairETHCHF = (MobileBy.ACCESSIBILITY_ID, "ETH/CHF")
    pairADAUSD = (MobileBy.ACCESSIBILITY_ID, "ADA/USD")
    pairADAEUR = (MobileBy.ACCESSIBILITY_ID, "ADA/EUR")
    pairADAGBP = (MobileBy.ACCESSIBILITY_ID, "ADA/GBP")
    pairADACHF = (MobileBy.ACCESSIBILITY_ID, "ADA/CHF")
    pairDOTUSD = (MobileBy.ACCESSIBILITY_ID, "DOT/USD")
    inputPrice = (MobileBy.XPATH, "//XCUIElementTypeTextField")
    buttonCreateAlert = (MobileBy.XPATH, "//XCUIElementTypeButton[@name = 'Create Alert']")

    def __init__(self, driver):
        super().__init__(driver)

    """
        Create Alert page actions
    """
    def get_create_alert_page_title(self, title):
        return self.get_text(title)

    def add_new_alert(self, currencyPair, price):
        self.click_on_element(currencyPair)
        self.send_keys(self.inputPrice, price)
        self.click_on_element(self.buttonCreateAlert)

    def add_new_alert_without_price(self, currencyPair):
        self.click_on_element(currencyPair)
        self.click_on_element(self.buttonCreateAlert)


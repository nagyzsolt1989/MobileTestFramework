from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class EditWatchlistPage(BasePage):
    """
        Edit Watchlist page locators
    """
    buttonBack = (MobileBy.ACCESSIBILITY_ID, "Back")
    titleEditWatchlist = (MobileBy.ACCESSIBILITY_ID, "Edit Watchlist")
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

    def __init__(self, driver):
        super().__init__(driver)

    """
        Edit Watchlist page actions
    """

    def get_edit_watchlist_page_title(self, title):
        return self.get_text(title)

    def select_pair(self, currencyPair):
        self.click_on_element(currencyPair)
        self.click_on_element(self.buttonBack)

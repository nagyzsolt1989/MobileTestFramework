
from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage

class AlertsPage(BasePage):
    """
        Alerts page locators
    """
    titleAlerts = (MobileBy.ACCESSIBILITY_ID, "Watchlist")
    buttonAdd = (MobileBy.ACCESSIBILITY_ID, "add-icon")
    tabWatchlist = (MobileBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'Watchlist')]")
    tabAlerts = (MobileBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, 'Alerts')]")

    def __init__(self, driver):
        super().__init__(driver)

    """
        Alerts page actions
    """
    def get_alerts_page_title(self, title):
        return self.get_text(title)

    def add_new_item(self):
        self.wait_for_element(self.buttonAdd)
        self.click_on_element(self.buttonAdd)

    def navigate_to_watchlist_tab(self):
        self.wait_for_element(self.tabWatchlist)
        self.click_on_element(self.tabWatchlist)

    def is_alert_displayed(self, currencyPair, price):
        alertLocator = (MobileBy.XPATH, "//XCUIElementTypeStaticText[contains(@name, '" + currencyPair +
                        "') and contains(@name, '" + price + "')]")
        return self.wait_for_element(alertLocator)

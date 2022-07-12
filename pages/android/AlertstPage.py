from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class AlertsPage(BasePage):
    """
        Alerts page locators
    """
    titleAlerts = (MobileBy.ACCESSIBILITY_ID, "Watchlist")
    buttonAdd = (MobileBy.XPATH, "//android.view.View[@content-desc='Alerts']/following-sibling::" +
                 "android.widget.Button[@content-desc='add-icon']")
    tabWatchlist = (MobileBy.XPATH, "//android.view.View/android.view.View[contains(@content-desc,'Watchlist')" +
                    "and contains(@content-desc,'Tab')]")
    tabAlerts = (MobileBy.XPATH, "//android.view.View[contains(@content-desc,'Alerts') " +
                 "and contains(@content-desc,'Tab')]")

    def __init__(self, driver):
        super().__init__(driver)

    """
        Alerts page actions
    """
    def get_alerts_page_title(self, title):
        return self.get_text(title)

    def wait_for_alert_title(self):
        self.wait_for_element(self.titleAlerts)

    def add_new_item(self):
        self.click_on_element(self.buttonAdd)

    def navigate_to_watchlist_tab(self):
        self.wait_for_element(self.tabWatchlist)
        self.click_on_element(self.tabWatchlist)

    def is_alert_displayed(self, currencyPair, price):
        alertLocator = (MobileBy.XPATH, "//android.view.View[contains(@content-desc,'" + currencyPair +
                        "') and  contains(@content-desc,'" + price + "')]")
        return self.wait_for_element(alertLocator)

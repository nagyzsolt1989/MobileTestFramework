from appium.webdriver.common.mobileby import MobileBy
from pages.BasePage import BasePage


class WatchlistPage(BasePage):
    """
        Watchlist page locators
    """
    titleWatchlist = (MobileBy.ACCESSIBILITY_ID, "Watchlist")
    buttonAdd = (MobileBy.ACCESSIBILITY_ID, "add-icon")
    tabWatchlist = (MobileBy.XPATH, "//android.view.View[contains(@content-desc, 'Watchlist')]")
    tabAlerts = (MobileBy.XPATH, "//android.view.View[contains(@content-desc, 'Alerts')]")

    def __init__(self, driver):
        super().__init__(driver)

    """
        Watchlist page actions
    """

    def get_watchlist_page_title(self, title):
        return self.get_text(title)

    def add_new_item(self):
        self.click_on_element(self.buttonAdd)

    def is_watchlist_empty(self):
        if (len(self.driver.find_elements(MobileBy.XPATH,
            "//android.view.View[contains(@content-desc, 'Watchlist')]//parent::android.view.View/preceding-sibling::android.view.View/android.view.View/android.view.View")) > 0):
            return False
        else:
            return True

    def is_currency_pair_displayed(self, currencyPair):
        return self.wait_for_element(currencyPair)

    def navigate_to_alerts_tab(self):
        self.click_on_element(self.tabAlerts)

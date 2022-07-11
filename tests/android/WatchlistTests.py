import time

from appium.webdriver.common.appiumby import AppiumBy

from pages.android.EditWatchlistPage import EditWatchlistPage
from pages.android.WatchListPage import WatchlistPage
from pages.android.AlertstPage import AlertsPage
from tests.android.AndroidBaseTest import AndroidBaseTest


class WatchlistTests(AndroidBaseTest):

    def __init__(self, driver):
        super().__init__(driver)

    def test_add_single_watchlist_item(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)

        self.assertTrue(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BTC/EUR").is_displayed(),
                        "BTC/EUR pair wasn't visible on the watchlist")

    def test_add_multiple_watchlist_items(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCUSD)
        self.editWatchlist.select_pair(EditWatchlistPage.pairETHEUR)

        self.assertTrue(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BTC/EUR").is_displayed(),
                        "BTC/USD pair wasn't visible on the watchlist")
        self.assertTrue(self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "BTC/EUR").is_displayed(),
                        "ETH/EUR pair wasn't visible on the watchlist")

    def test_add_then_remove_watchlist_item(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)
        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)

        self.assertTrue(self.watchlist.is_watchlist_empty(), "Watchlist wasn't empty")

    # Possible bug
    def test_verify_watchlist_item_after_back_and_forth_navigation(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.navigate_to_watchlist_tab()

        self.assertTrue(self.watchlist.is_currency_pair_displayed(EditWatchlistPage.pairBTCEUR),
                        "BTC/EUR pair wasn't visible after a back and forth navigation")

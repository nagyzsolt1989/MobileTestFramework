import pytest
from pages.android.EditWatchlistPage import EditWatchlistPage
from pages.android.WatchlistPage import WatchlistPage
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
        self.editWatchlist.navigate_back()

        assert True == self.watchlist.is_currency_pair_displayed(EditWatchlistPage.pairBTCEUR), \
                        "BTC/EUR pair wasn't visible on the watchlist"

    def test_add_multiple_watchlist_items(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCUSD)
        self.editWatchlist.select_pair(EditWatchlistPage.pairETHEUR)
        self.editWatchlist.select_pair(EditWatchlistPage.pairDOTUSD)
        self.editWatchlist.navigate_back()

        assert True == self.watchlist.is_currency_pair_displayed(EditWatchlistPage.pairBTCUSD), \
                        "BTC/USD pair wasn't visible on the watchlist"
        assert True == self.watchlist.is_currency_pair_displayed(EditWatchlistPage.pairETHEUR), \
                        "BTC/EUR pair wasn't visible on the watchlist"
        assert True == self.watchlist.is_currency_pair_displayed(EditWatchlistPage.pairDOTUSD), \
                        "DOT/USD pair wasn't visible on the watchlist"

    def test_add_then_remove_watchlist_item(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)
        self.editWatchlist.navigate_back()
        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)
        self.editWatchlist.navigate_back()

        assert True == self.watchlist.is_watchlist_empty(), "Watchlist wasn't empty"

    @pytest.mark.xfail(condition=lambda: True, reason='possible bug')
    def test_verify_watchlist_item_after_back_and_forth_navigation(self):
        self.watchlist = WatchlistPage(self.driver)
        self.editWatchlist = EditWatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)

        self.watchlist.add_new_item()
        self.editWatchlist.select_pair(EditWatchlistPage.pairBTCEUR)
        self.editWatchlist.navigate_back()

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.navigate_to_watchlist_tab()

        assert True == self.watchlist.is_currency_pair_displayed(EditWatchlistPage.pairBTCEUR), \
                        "BTC/EUR pair wasn't visible after a back and forth navigation"

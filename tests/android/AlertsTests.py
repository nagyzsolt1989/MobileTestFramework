import pytest

from pages.android.CreateAlertPage import CreateAlertPage
from pages.android.WatchlistPage import WatchlistPage
from pages.android.AlertstPage import AlertsPage
from tests.android.AndroidBaseTest import AndroidBaseTest


class AlertsTests(AndroidBaseTest):

    def __init__(self, driver):
        super().__init__(driver)

    def test_add_single_alert(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.wait_for_alert_title()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCEUR, 100)

        assert True == self.alerts.is_alert_displayed("BTC/EUR", "100.0"), \
            "BTC/EUR alert with 100.0 price isn't displayed"

    def test_add_multiple_alerts(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCUSD, 5)
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCUSD, 10)

        assert True == self.alerts.is_alert_displayed("BTC/USD", "5.0"), "BTC/USD alert with 5.0 price isn't displayed"
        assert True == self.alerts.is_alert_displayed("BTC/USD", "10.0"), \
            "BTC/USD alert with 10.0 price isn't displayed"

    def test_add_alert_without_a_price(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert_without_price(CreateAlertPage.pairBTCEUR)

        assert True == self.alerts.is_alert_displayed("BTC/EUR", "0.0"), "BTC/EUR alert with 0.0 price isn't displayed"

    def test_add_alert_with_invalid_characters(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCEUR, "1!!!!????")

        assert True == self.alerts.is_alert_displayed("BTC/EUR", "0.0"), "BTC/EUR alert with 0.0 price isn't displayed"

    @pytest.mark.xfail(condition=lambda: True, reason='possible bug')
    def test_add_alert_with_negative_price(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCEUR, "-100.5")

        assert True == self.alerts.is_alert_displayed("BTC/EUR", "-100.5"), \
            "BTC/EUR alert with -100.0 price isn't displayed"

    def test_add_alert_with_text(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCEUR, "test")

        assert True == self.alerts.is_alert_displayed("BTC/EUR", "0.0"), "BTC/EUR alert with 0.0 price isn't displayed"

    def test_add_alert_with_SQL_injection(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCUSD, 5)
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCEUR, "; DROP TABLE ALERTS;")

        assert True == self.alerts.is_alert_displayed("BTC/USD", "5.0"), "BTC/USD alert with 5.0 price isn't displayed"
        assert True == self.alerts.is_alert_displayed("BTC/EUR", "0.0"), "ETH/EUR alert with 0.0 price isn't displayed"

    @pytest.mark.xfail(condition=lambda: True, reason='possible bug')
    def test_verify_alert_after_back_and_forth_navigation(self):
        self.watchlist = WatchlistPage(self.driver)
        self.alerts = AlertsPage(self.driver)
        self.createAlert = CreateAlertPage(self.driver)

        self.watchlist.navigate_to_alerts_tab()
        self.alerts.add_new_item()
        self.createAlert.add_new_alert(CreateAlertPage.pairBTCUSD, 5)
        self.alerts.navigate_to_watchlist_tab()
        self.watchlist.navigate_to_alerts_tab()

        assert True == self.alerts.is_alert_displayed("BTC/USD", "5.0"), "BTC/USD alert with 5.0 price isn't displayed"

import time

import pytest

from tests.android.AndroidBaseTest import AndroidBaseTest

class AlertsTests(AndroidBaseTest):

    def __init__(self, driver):
        super().__init__(driver)

    def test_install(self):
        time.sleep(10)


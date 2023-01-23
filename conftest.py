from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
import logging
import pytest
import os


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default="ios", help="Select a platform: android / ios")
    parser.addoption('--device', action='store', default="emulator",
                     help="Select a device type: simulator / emulator / real device")


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


@pytest.fixture(autouse=True)
def mobile_driver(request):
    logger = logging.getLogger(__name__)
    logger.info("Configuring Appium options")
    if "android" == request.config.getoption("--platform"):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platformVersion = '12'
        options.device_name = 'Google Pixel 6'
        options.app = os.path.dirname(os.path.dirname(__file__)) + "/MobileTestFramework/apps/demoApp.apk"
        options.app_wait_activity = "dev.flutter.formApp.form_app.MainActivity"
    elif "ios" == request.config.getoption("--platform"):
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.platformVersion = '15.6'
        options.device_name = 'iPhone 14'
        options.app = os.path.dirname(os.path.dirname(__file__)) + "/MobileTestFramework/apps/demoApp.zip"

    driver = webdriver.Remote("http://0.0.0.0:4723", options=options)
    logger.info("Appium driver initialized")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
    logger.info("Appium session ended")

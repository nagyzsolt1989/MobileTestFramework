import logging
import os

import pytest
from appium import webdriver


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default="android", help="Select a platform: android / ios")
    parser.addoption('--device', action='store', default="emulator",
                     help="Select a device type: simulator / emulator / real device")


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


@pytest.fixture(scope='session')
def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.FileHandler(r'app.log', mode='w')
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


@pytest.fixture(scope='class', autouse=True)
def mobile_driver(request, get_logger):
    if ("android" == request.config.getoption("--platform")):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "12",
            "automationName": "UiAutomator2",
            "deviceName": "Google Pixel 6",
            "app": os.path.dirname(os.path.dirname(__file__)) + "/MobileTestFramework/apps/demoApp.apk",
            "appWaitActivity": "dev.flutter.formApp.form_app.MainActivity"
        }
    elif ("ios" == request.config.getoption("--platform")):
        desired_caps = {
            "platformName": "iOS",
            "platformVersion": "16.2",
            "automationName": "XCUITest",
            "deviceName": "iPhone 14",
            "app": os.path.dirname(os.path.dirname(__file__)) + "MobileTestFramework/apps/demoApp.zip"
        }

    driver = webdriver.Remote("http://0.0.0.0:4723", desired_caps)
    logging.info("Appium driver ")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()

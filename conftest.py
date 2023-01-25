from utils.slack.slack_notification import web_hook, send_slack_notification, compose_message
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from utils.listeners.event_listener import EventListener
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
import logging
import pytest
import time
import math
import os

logger = logging.getLogger(__name__)


@pytest.hookimpl
def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default="ios", help="Select a platform: android / ios")
    parser.addoption('--device', action='store', default="emulator",
                     help="Select a device type: simulator / emulator / real device")
    parser.addoption('--slack', action='store', default="true", help="Enable Slack integration: true / false")


@pytest.fixture(scope="session")
def app(request):
    return request.config.getoption("--app")


@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")


@pytest.fixture(autouse=True)
def mobile_driver(request):
    logger.info("Configuring Appium options")
    if "android" == request.config.getoption("--platform"):
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.platform_version = '12'
        options.device_name = 'Google Pixel 6'
        options.app = os.path.dirname(os.path.dirname(__file__)) + "/MobileTestFramework/apps/demoApp.apk"
        options.app_wait_activity = "dev.flutter.formApp.form_app.MainActivity"
    elif "ios" == request.config.getoption("--platform"):
        options = XCUITestOptions()
        options.platform_name = "iOS"
        options.platform_version = '15.6'
        options.device_name = 'iPhone 14'
        options.app = os.path.dirname(os.path.dirname(__file__)) + "/MobileTestFramework/apps/demoApp.zip"

    global device_name, platform, platform_version
    device_name = options.device_name
    platform = options.platform_name
    platform_version = options.platform_version

    driver = EventFiringWebDriver(webdriver.Remote("http://0.0.0.0:4723", options=options), EventListener())
    driver.implicitly_wait(10)
    request.cls.driver = driver
    logger.info("Appium driver initialized")
    yield
    driver.quit()
    logger.info("Appium session ended")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        'failed_cases': [report.nodeid.split('::')[-1] for report in terminalreporter.stats.get('failed', [])],
        'duration': time.time() - terminalreporter._sessionstarttime
    }

    minutes, seconds = divmod(result["duration"], 60)
    minutes, seconds = int(minutes), math.trunc(seconds)
    duration = str(minutes) + " minute(s) " + str(seconds) + " seconds"

    if len(result["failed_cases"]) > 0:
        failed_cases_list = "\n\u2022 " + '\n\u2022'.join([str(case) for case in result["failed_cases"]])
    else:
        failed_cases_list = "\n\u2022 None"

    message = compose_message(platform, device_name,
                              platform_version, result["passed"], result["failed"], result["skipped"],
                              result["total"], duration, failed_cases_list)

    if config.getoption('--slack') == "true":
        send_slack_notification(web_hook, message)
        logger.info("Slack notification sent")

import logging as logger
import time

from selenium.common import TimeoutException
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_on_element(self, MobilBy):
        self.wait.until(EC.visibility_of_element_located(MobilBy)).click()

    def send_keys(self, MobilBy, text):
        self.wait.until(EC.visibility_of_element_located(MobilBy)).send_keys(text)

    def wait_for_element(self, MobilBy):
        try:
            self.wait.until(EC.visibility_of_element_located(MobilBy))
            return True
        except TimeoutException:
            logger.info("%s hasn't been visible", MobilBy)
            return False

    def get_text(self, title):
        self.wait.until(EC.title_is(title))
        return self.driver.title

from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from allure_commons.types import AttachmentType
import allure


class EventListener(AbstractEventListener):

    def before_click(self, element, driver):
        allure.attach(driver.get_screenshot_as_png(), "Before clicking on " + element.text, AttachmentType.PNG)
        super().before_click(element, driver)

    def before_change_value_of(self, element, driver):
        allure.attach(driver.get_screenshot_as_png(), "Before changing value of " + element.text,AttachmentType.PNG)
        super().before_change_value_of(element, driver)

    def on_exception(self, exception, driver):
        allure.attach(driver.get_screenshot_as_png(), "TEST FAILURE!", AttachmentType.PNG)
        super().on_exception(exception, driver)

from appium.webdriver.common.mobileby import MobileBy
from framework.core.page_base import BasePage


class HomePage(BasePage):
    """
    Home page locators
    """

    label_form_samples = (MobileBy.ACCESSIBILITY_ID, "Form Samples")
    button_sign_in_with_http = (MobileBy.ACCESSIBILITY_ID, "Sign in with HTTP")
    button_autofill = (MobileBy.ACCESSIBILITY_ID, "Autofill")
    button_form_widgets = (MobileBy.ACCESSIBILITY_ID, "Form widgets")
    button_validation = (MobileBy.ACCESSIBILITY_ID, "Validation")

    def __init__(self, driver):
        super().__init__(driver)

    def is_form_samples_label_displayed(self):
        return self.wait_for_element(self.label_form_samples)

    def is_sign_in_with_http_button_displayed(self):
        return self.wait_for_element(self.button_sign_in_with_http)

    def is_autofill_button_displayed(self):
        return self.wait_for_element(self.button_autofill)

    def is_form_widget_button_displayed(self):
        return self.wait_for_element(self.button_form_widgets)

    def is_validation_button_displayed(self):
        return self.wait_for_element(self.button_validation)

    def click_on_sign_in_with_http_button(self):
        self.click_on_element(self.button_sign_in_with_http)
        self.logger.info("Home Page - Sign in with HTTP button clicked")

    def click_on_validation_button(self):
        self.click_on_element(self.button_validation)
        self.logger.info("Home Page - Validation button clicked")

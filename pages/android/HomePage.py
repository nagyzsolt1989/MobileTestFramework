from appium.webdriver.common.mobileby import MobileBy
from framework.core.BasePage import BasePage


class HomePage(BasePage):
    """
    Home page locators
    """

    labelFormSamples = (MobileBy.ACCESSIBILITY_ID, "Form Samples")
    buttonSignInWithHTTP = (MobileBy.ACCESSIBILITY_ID, "Sign in with HTTP")
    buttonAutoFill = (MobileBy.ACCESSIBILITY_ID, "Autofill")
    buttonFormWidgets = (MobileBy.ACCESSIBILITY_ID, "Form widgets")
    buttonValidation = (MobileBy.ACCESSIBILITY_ID, "Validation")

    def __init__(self, driver):
        super().__init__(driver)

    def is_form_samples_label_displayed(self):
        return self.wait_for_element(self.labelFormSamples)

    def is_sign_in_with_http_button_displayed(self):
        return self.wait_for_element(self.buttonSignInWithHTTP)

    def is_autofill_button_displayed(self):
        return self.wait_for_element(self.buttonAutoFill)

    def is_form_widget_button_displayed(self):
        return self.wait_for_element(self.buttonFormWidgets)

    def is_validation_button_displayed(self):
        return self.wait_for_element(self.buttonValidation)

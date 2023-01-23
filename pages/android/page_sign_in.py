from appium.webdriver.common.mobileby import MobileBy
from framework.core.page_base import BasePage


class SignInPage(BasePage):
    """
    Sign In page locators
    """

    input_username = (MobileBy.XPATH, "//android.widget.EditText[@text='Email\nYour email address']")
    input_password = (MobileBy.XPATH, "//android.widget.EditText[@text='Password']")
    button_sign_in = (MobileBy.ACCESSIBILITY_ID, "Sign in")
    label_unable_to_sign_in = (MobileBy.ACCESSIBILITY_ID, "Unable to sign in.")
    button_ok = (MobileBy.ACCESSIBILITY_ID, "OK")

    def __init__(self, driver):
        super().__init__(driver)

    def is_user_input_field_displayed(self):
        return self.wait_for_element(self.input_username)

    def is_password_input_field_displayed(self):
        return self.wait_for_element(self.input_password)

    def is_sign_in_button_displayed(self):
        return self.wait_for_element(self.button_sign_in)

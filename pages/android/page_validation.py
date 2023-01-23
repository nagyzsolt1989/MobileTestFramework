from appium.webdriver.common.mobileby import MobileBy
from framework.core.page_base import BasePage


class ValidationPage(BasePage):
    """
    Validation page locators
    """

    label_story_generator = (MobileBy.ACCESSIBILITY_ID, "📖 Story Generator")
    input_adjective = (MobileBy.XPATH, "//android.widget.EditText[1]")
    input_noun = (MobileBy.XPATH, "//android.widget.EditText[2]")
    checkbox_terms_of_service = (MobileBy.XPATH, "//android.widget.CheckBox")
    button_submit = (MobileBy.ACCESSIBILITY_ID, "Submit")
    warning_adjective = (MobileBy.ACCESSIBILITY_ID, "Please enter an adjective.")
    warning_noun = (MobileBy.ACCESSIBILITY_ID, "Please enter a noun.")
    warning_terms_of_service = (MobileBy.ACCESSIBILITY_ID, "You must agree to the terms of service.")
    label_your_story = (MobileBy.ACCESSIBILITY_ID, "Your story")
    text_your_story = (MobileBy.ACCESSIBILITY_ID, "The new developer saw a cat")
    button_done = (MobileBy.ACCESSIBILITY_ID, "Done")

    def __init__(self, driver):
        super().__init__(driver)

    def is_story_generator_label_displayed(self):
        return self.wait_for_element(self.label_story_generator)

    def is_adjective_input_field_displayed(self):
        return self.wait_for_element(self.input_adjective)

    def is_noun_input_field_displayed(self):
        return self.wait_for_element(self.input_noun)

    def is_terms_of_service_checkbox_displayed(self):
        return self.wait_for_element(self.checkbox_terms_of_service)

    def is_submit_button_displayed(self):
        return self.wait_for_element(self.button_submit)

    def is_adjective_warning_displayed(self):
        return self.wait_for_element(self.warning_adjective)

    def is_noun_warning_displayed(self):
        return self.wait_for_element(self.warning_noun)

    def is_terms_of_service_warning_displayed(self):
        return self.wait_for_element(self.warning_terms_of_service)

    def is_your_story_label_displayed(self):
        return self.wait_for_element(self.label_your_story)

    def is_your_story_text_displayed(self):
        return self.wait_for_element(self.text_your_story)

    def is_done_button_displayed(self):
        return self.wait_for_element(self.button_done)

    def click_on_submit_button(self):
        self.click_on_element(self.button_submit)
        self.logger.info("Validation Page - Submit button clicked")

    def fill_adjective_field(self, adjective):
        self.send_keys(self.input_adjective, adjective)
        self.logger.info("%s is changed to: %s", self.input_adjective, adjective)

    def fill_noun_field(self, noun):
        self.click_on_element(self.input_noun)
        self.send_keys(self.input_noun, noun)
        self.logger.info("%s is changed to: %s", self.input_noun, noun)

    def accept_terms_of_service(self):
        self.click_on_element(self.checkbox_terms_of_service)
        self.logger.info("Terms of service accepted")

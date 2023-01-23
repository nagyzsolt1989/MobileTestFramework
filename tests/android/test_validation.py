from pages.android.page_validation import ValidationPage
from framework.core.test_base import BaseTest
from pages.android.page_home import HomePage


class TestValidation(BaseTest):

    def test_validation_page(self):
        self.home = HomePage(self.driver)
        self.validation = ValidationPage(self.driver)

        self.home.click_on_validation_button()

        assert True is self.validation.is_story_generator_label_displayed(), "Story Generator label was not visible"
        assert True is self.validation.is_adjective_input_field_displayed(), "Adjective input field was not visible"
        assert True is self.validation.is_noun_input_field_displayed(), "Noun input field was not visible"
        assert True is self.validation.is_terms_of_service_checkbox_displayed(), \
            "Terms of service checkbox was not visible"
        assert True is self.validation.is_submit_button_displayed(), "Submit button was not visible"

    def test_empty_story(self):
        self.home = HomePage(self.driver)
        self.validation = ValidationPage(self.driver)

        self.home.click_on_validation_button()
        self.validation.click_on_submit_button()

        assert True is self.validation.is_adjective_warning_displayed(), "Adjective warning was not visible"
        assert True is self.validation.is_noun_warning_displayed(), "Noun warning was not visible"
        assert True is self.validation.is_terms_of_service_warning_displayed(), \
            "Terms of Service warning was not visible"

    def test_valid_story(self):
        self.home = HomePage(self.driver)
        self.validation = ValidationPage(self.driver)

        self.home.click_on_validation_button()
        self.validation.fill_adjective_field("new")
        self.validation.fill_noun_field("cat")
        self.validation.accept_terms_of_service()
        self.validation.click_on_submit_button()

        assert True is self.validation.is_your_story_label_displayed(), "Your Story label was not visible"
        assert True is self.validation.is_your_story_text_displayed(), "Your Story text was not visible"
        assert True is self.validation.is_done_button_displayed(), "Done button was not visible"

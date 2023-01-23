from framework.core.test_base import BaseTest
from pages.ios.page_home import HomePage


class TestHome(BaseTest):

    def test_home_page(self):
        home = HomePage(self.driver)

        assert True is home.is_form_samples_label_displayed(), "Form Samples label was not visible"
        assert True is home.is_sign_in_with_http_button_displayed(), "Sign in with HTTP button was not visible"
        assert True is home.is_autofill_button_displayed(), "Autofill button was not visible"
        assert True is home.is_form_widget_button_displayed(), "Form Widgets button was not visible"
        assert True is home.is_validation_button_displayed(), "Validation button was not visible"

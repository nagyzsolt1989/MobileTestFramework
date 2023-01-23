from pages.android.page_sign_in import SignInPage
from framework.core.test_base import BaseTest
from pages.android.page_home import HomePage
import allure


@allure.feature('Sign In')
@allure.story('Layout')
class TestSignIn(BaseTest):

    def test_home_page(self):
        self.home = HomePage(self.driver)
        self.sign_in = SignInPage(self.driver)

        self.home.click_on_sign_in_with_http_button()

        assert True is self.sign_in.is_user_input_field_displayed(), "Username input field was not visible"
        assert True is self.sign_in.is_password_input_field_displayed(), "Password input field was not visible"
        assert True is self.sign_in.is_sign_in_button_displayed(), "Sign In button was not visible"

from Pages.base_page import BasePage
from Locators.locators import *


class LoginPage(BasePage):
    _username_input = {"by": By.ID, "value": "userSignInFormEmail"}
    _password_input = {"by": By.ID, "value": "user_password"}
    _signin_button = {"by": By.CSS_SELECTOR, "value": "input.gr-button.gr-button--dark"}
    _login_failure = {"by": By.CSS_SELECTOR, "value": "#emailForm > div > div"}

    def __init__(self, driver):
        self.driver = driver

    def with_(self, username, password):
        self._type(LoginPageLocators._username_input, username)
        self._type(LoginPageLocators._password_input, password)
        self._click(LoginPageLocators._signin_button)

    def failure_message_present(self):
        return self._is_displayed(LoginPageLocators._login_failure)
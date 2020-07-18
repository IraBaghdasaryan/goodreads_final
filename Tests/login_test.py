from Pages.login_page import LoginPage
from Pages.home_page import HomePage
import pytest
from Tests.data_storage import *

#Check login functionality
#Check system behavior when valid email and password is entered.

class Test_Login():
    def test_valid_login(self, browser):
        login_pg = LoginPage(browser)
        home_pg = HomePage(browser)
        browser.get("https://www.goodreads.com/")
        login_pg.with_(correct_username, correct_password)
        home_pg.success_message_present()

#Check system behavior when 1. invalid email and password is entered, 2. valid email invalid password, 3 invalid email, valid password
#I used parametrize testing for invalid login test

    @pytest.mark.parametrize("username, password", list_wrong_pass)
    def test_wrong_pass(self, username, password, browser):
        browser.get("https://www.goodreads.com/")
        login_pg = LoginPage(browser)
        login_pg.with_(username, password)
        assert login_pg.failure_message_present()
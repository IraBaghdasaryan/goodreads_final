from Pages.base_page import BasePage
from Locators.locators import *

class HomePageLocators:
    _login_success ={"by": By.CSS_SELECTOR, "value": "body > div.gr-mainContentContainer"}
    _menu = {"by":By.CLASS_NAME, "value": "siteHeader__topLevelItem"}
    _mybooks = {"by": By.LINK_TEXT, "value": "My Books"}
    _display = {"by": By.CSS_SELECTOR, "value": "body > div.gr-mainContentContainer"}


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def success_message_present(self):
        self._wait_for_element(HomePageLocators._display)

    def Menu(self):
        self._find(HomePageLocators._menu)


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Locators.locators import HeaderLocators
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class HeaderLocator:
    _search_box = {"by": By.CSS_SELECTOR, "value": "input.searchBox__input.searchBox__input--navbar"}
    _search_button = {"by": By.XPATH, "value": "div[2]/form/button"}
    _search_displayed = {"by": By.CSS_SELECTOR, "value": "div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > h3"}


class Header(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def searching_book(self):
        self._click(HeaderLocators._search_button)

    def search_input(self, search):
        self._type(HeaderLocators._search_box, search)
        self._find(HeaderLocators._search_box).send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver,10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > h3")))



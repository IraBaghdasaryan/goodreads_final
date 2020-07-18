from Pages.base_page import BasePage
from Locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BookFromListLocators:
    want_to_read = {"by": By.XPATH, "value": "/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/form/button"}


class SelectedBook(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def add_to_read(self):
        self._click(BookFromListLocators.want_to_read)

    def mybook(self):
        self._click(HomePageLocators._mybooks)
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#books")))

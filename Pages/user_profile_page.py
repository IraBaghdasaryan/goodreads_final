from Pages.base_page import BasePage
from Locators.locators import *

class UserBooksLocator:
    _empty_shelf = {"by": By.CSS_SELECTOR, "value": "div.greyText.nocontent.stacked"}
    _present_books_in_shelf= {"by": By.CSS_SELECTOR, "value": "#booksBody"}
    _Lotr_first = {"by": By.XPATH, "value": "/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[6]/table/tbody/tr/td[4]/div/a"}
    _delete_book = {"by": By.XPATH, "value": "/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[6]/table/tbody/tr/td[30]/div/div/a"}


class UserBooks(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def present_books(self):
        self._find(UserBooksLocators._present_books_in_shelf)

    def delete_book(self):
        self._click(UserBooksLocators._delete_book)

    def verify_empty_shelf(self):
        self._find(UserBooksLocators._empty_shelf)

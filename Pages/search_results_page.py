from Locators.locators import *
from Pages.base_page import BasePage

class SearchResultsLocators:
    _list_book = {"by": By.TAG_NAME, "value": "td"}


class Search_Page(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def list_of_books(self):
        self._findlist(SearchResultsLocators._list_book)








        #List<WebElement> listofElements = self.driver.findElements(By)

    def choose_book(self):
        self._click(Search_LOTR._lotr1)

        #wait = WebDriverWait(self.driver, 10)
        #return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#topcol")))
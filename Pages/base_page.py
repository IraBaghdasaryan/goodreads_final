from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class BasePage():
    def _init__(self, driver):
        self.driver = driver

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _findlist(self, locator):
        return self.driver.find_elements(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _is_displayed(self, locator):
        return self._find(locator).is_displayed()

    def _type(self, locator, input_test):
        self._find(locator).send_keys(input_test)

    def _wait_for_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located((locator["by"], locator["value"])))

    def _visit(self, url):
        self.driver.get(url)


from typing import Tuple

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverKeywords:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)

    def click_by_locator(self, locator: Tuple[str, str]):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def type_by_locator(self, locator: Tuple[str, str], text):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def get_text_by_locator(self, locator: Tuple[str, str]):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text


import pytest
from selenium import webdriver

""" """
class AutomationWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # below code runs before each test method
        browser = "edge"
        if browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(0)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        # below code runs after each test method
        self.driver.quit()

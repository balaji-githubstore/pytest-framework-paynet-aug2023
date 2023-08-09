import pytest
from selenium import webdriver


class AutomationWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # below code runs before each test method
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        # below code runs after each test method
        self.driver.quit()
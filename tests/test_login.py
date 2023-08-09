from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.webdriver_wrapper import AutomationWrapper


class TestLogin(AutomationWrapper):
    def test_valid_login(self):
        self.driver.find_element(By.ID, "authUser").send_keys("physician")
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("physician")
        select_language = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_language.select_by_visible_text("English (Indian)")
        self.driver.find_element(By.ID, "login-button").click()
        assert_that(self.driver.title).is_equal_to("OpenEMR")

    def test_invalid_login(self):
        self.driver.find_element(By.ID, "authUser").send_keys("john")
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("john123")
        select_language = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_language.select_by_visible_text("English (Indian)")
        self.driver.find_element(By.ID, "login-button").click()
        actual_error=self.driver.find_element(By.XPATH,"//p[contains(text(),'Invalid')]").text
        assert_that(actual_error).is_equal_to("Invalid username or password")



class TestLoginUI(AutomationWrapper):
    def test_title(self):
        assert_that(self.driver.title).is_equal_to("OpenEMR Login")

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record")

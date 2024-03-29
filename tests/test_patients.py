from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base.webdriver_wrapper import AutomationWrapper


class TestPatient(AutomationWrapper):
    def test_add_valid_patient(self):
        self.driver.find_element(By.ID, "authUser").send_keys("admin")
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys("pass")
        select_language = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_language.select_by_visible_text("English (Indian)")
        self.driver.find_element(By.ID, "login-button").click()
        # click on patient
        self.driver.find_element(By.XPATH,"//div[text()='Patient']").click()
        # click on new/search
        self.driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
        # enter firstname as john
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@name='pat']"))

        self.driver.find_element(By.ID, "form_fname").send_keys("john")
        self.driver.find_element(By.ID, "form_lname").send_keys("wick")
        self.driver.find_element(By.ID, "form_DOB").send_keys("2023-08-08")
        Select(self.driver.find_element(By.ID,"form_sex")).select_by_visible_text("Male")
        self.driver.find_element(By.ID,"create").click()

        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,"//iframe[@id='modalframe']"))
        self.driver.find_element(By.XPATH,"//button[text()='Confirm Create New Patient']").click()
        self.driver.switch_to.default_content()

        wait = WebDriverWait(self.driver, 40)
        wait.until(expected_conditions.alert_is_present())

        # get the alert text and print it
        actual_alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()

        # check for presence of element
        if len(self.driver.find_elements(By.XPATH,"//div[@class='closeDlgIframe']"))>0:
            self.driver.find_element(By.XPATH,"//div[@class='closeDlgIframe']").click()

        assert_that(actual_alert_text).contains("Tobacco")
        # Assert the text displayed - Medical Record Dashboard - john wick
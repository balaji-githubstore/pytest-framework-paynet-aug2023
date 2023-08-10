from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class MainPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_main_page_title(self):
        return self.driver.title

    def click_on_patient_menu(self):
        self.driver.find_element(By.XPATH, "//div[text()='Patient']").click()

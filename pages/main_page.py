from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_main_page_title(self):
        return self.driver.title

    def click_on_patient_menu(self):
        self.driver.find_element(By.XPATH, "//div[text()='Patient']").click()
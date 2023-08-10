from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    def select_language(self, language):
        select_language = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_language.select_by_visible_text(language)

    def click_on_login(self):
        self.driver.find_element(By.ID, "login-button").click()

    def get_invalid_error_message(self):
        return self.driver.find_element(By.XPATH, "//p[contains(text(),'Invalid')]").text

    @property
    def get_login_page_title(self):
        return self.driver.title

    def get_application_description(self):
        return self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
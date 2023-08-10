from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__username_locator=(By.ID, "authUser")
        self.__password_locator=(By.CSS_SELECTOR, "#clearPass")
        self.__language_locator=(By.XPATH, "//select[@name='languageChoice']")
        self.__login_locator=(By.ID, "login-button")
        self.__error_locator=(By.ID, "login-button")

    def enter_username(self, username):
        super().type_by_locator(self.__username_locator,username)

    def enter_password(self, password):
        super().type_by_locator(self.__password_locator,password)

    def select_language(self, language):
        select_language = Select(self.driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
        select_language.select_by_visible_text(language)

    def click_on_login(self):
        super().click_by_locator(self.__login_locator)

    def get_invalid_error_message(self):
        return super().get_text_by_locator(self.__error_locator)

    @property
    def get_login_page_title(self):
        return self.driver.title

    def get_application_description(self):
        return self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text

    def get_username_placeholder(self):
        return super().get_attribute_value_by_locator(self.__username_locator,"placeholder")

    def get_password_placeholder(self):
        return super().get_attribute_value_by_locator(self.__password_locator,"placeholder")

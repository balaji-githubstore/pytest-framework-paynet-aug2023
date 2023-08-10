import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_wrapper import AutomationWrapper
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):
    @pytest.mark.parametrize(
        "username, password, language, expected_title", DataSource.test_valid_login_data_csv)
    def test_valid_login(self, username, password, language, expected_title):
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_language(language)
        login_page.click_on_login()

        main_page = MainPage(self.driver)
        assert_that(main_page.get_main_page_title()).is_equal_to(expected_title)

    @pytest.mark.parametrize("username,password,language,expected_error", DataSource.test_invalid_data)
    def test_invalid_login(self, username, password, language, expected_error):
        login_page = LoginPage(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_language(language)
        login_page.click_on_login()

        actual_error = login_page.get_invalid_error_message()
        assert_that(actual_error).is_equal_to(expected_error)


class TestLoginUI(AutomationWrapper):
    def test_title(self):
        login_page = LoginPage(self.driver)
        assert_that(login_page.get_login_page_title).is_equal_to("OpenEMR Login")

    def test_app_description(self):
        login_page = LoginPage(self.driver)
        assert_that(login_page.get_application_description()).contains("Electronic Health Record")

    def test_placeholder(self):
        login_page = LoginPage(self.driver)
        actual_username_placeholder = login_page.get_username_placeholder()
        actual_password_placeholder = login_page.get_password_placeholder()
        assert_that(actual_username_placeholder).is_equal_to("Username")
        assert_that(actual_password_placeholder).is_equal_to("Password")

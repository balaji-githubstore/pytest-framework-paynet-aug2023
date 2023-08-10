class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_main_page_title(self):
        return self.driver.title

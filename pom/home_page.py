from selenium.webdriver.common.by import By
from web.web_common import WebCommonMethods as Common


# this class contains HomePage web elements and methods
class HomePage:
    page_url = '#/home'

    user_name_field = (By.XPATH, "//div[@class='info']/h3")
    user_role_field = (By.XPATH, "//div[@class='info']/p")

    def __init__(self, driver):
        self.driver = driver

    def get_user_name_text(self):
        # this script will ensure loading of visible text
        Common.wait_for_element_visibility(HomePage.user_name_field, 3, self.driver)
        # this script calls common method, passes element as an argument and returns visible text
        return Common.get_text(Common.get_element(self.driver, HomePage.user_name_field))

    def get_user_role_text(self):
        # this script will ensure loading of visible text
        Common.wait_for_element_visibility(HomePage.user_role_field, 3, self.driver)
        # this script calls common method, passes element as an argument and returns visible text
        return Common.get_text(Common.get_element(self.driver, HomePage.user_role_field))



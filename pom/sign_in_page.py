from selenium.webdriver.common.by import By
from web.web_common import WebCommonMethods as Common


# this class contains SignInPage web elements and methods
class SignInPage:
    page_url = '/#/login'

    email_field = (By.ID, 'mat-input-0')
    password_field = (By.ID, 'mat-input-1')
    submit_button = (By.XPATH, "//button[@type='submit']")
    auth_failed_snack = (By.CSS_SELECTOR, "simple-snack-bar.mat-simple-snackbar")

    def __init__(self, driver):
        self.driver = driver

    def fill_out_email_field(self, text):
        # this script calls common method and passes element and text as argument
        Common.input_field(Common.get_element(self.driver, SignInPage.email_field), text)

    def fill_out_password_field(self, text):
        # this script calls common method and passes element and text as argument
        Common.input_field(Common.get_element(self.driver, SignInPage.password_field), text)

    def click_submit_button(self):
        # this script calls common method and passes element as argument
        Common.click_element(Common.get_element(self.driver, SignInPage.submit_button))

    def get_auth_failed_snack_text(self):
        # this script will ensure loading of visible text
        Common.wait_for_element_visibility(SignInPage.auth_failed_snack, 3, self.driver)
        # this script calls common method, passes element as an argument and returns visible text
        return Common.get_text(Common.get_element(self.driver, SignInPage.auth_failed_snack))







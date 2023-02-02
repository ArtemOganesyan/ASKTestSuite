import pytest

import config
from utilities import logger
from utilities.test_data import get_test_data
from pom.common_page import CommonPage


# this test suit verifies login form functionality for teacher and student users
class TestSignIn:
    logger = logger.get_logger()

    #  teacher sign in with valid credentials
    @pytest.mark.positive
    def test_sign_in_teacher_positive(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        # this will create object with attributes being instances of all application pages
        page = CommonPage(driver)
        self.logger.debug("getting test data")
        # this will get test data from json file based on test type, test suit, test case
        test_data = get_test_data('web', 'TestSignIn', 'sign_in_teacher_positive')

        self.logger.debug(f"navigating to url: {config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        driver.get(f"{config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        self.logger.debug("filling out email field")
        page.sign_in_page.fill_out_email_field(test_data['email'])
        self.logger.debug("filling out password field")
        page.sign_in_page.fill_out_password_field(test_data['password'])
        self.logger.debug("clicking submit button")
        page.sign_in_page.click_submit_button()

        self.logger.debug("getting user name")
        actual_user_name = page.homepage.get_user_name_text()
        self.logger.debug("getting user role")
        actual_user_role = page.homepage.get_user_role_text()
        self.logger.debug("asserting user role")
        assert actual_user_role == 'TEACHER'
        self.logger.debug("asserting user name")
        assert actual_user_name == 'Professor Freeman'

    #  teacher sign in with invalid credentials
    def test_sign_in_teacher_negative(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        page = CommonPage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('web', 'TestSignIn', 'sign_in_teacher_negative')

        self.logger.debug(f"navigating to url: {config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        driver.get(f"{config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        self.logger.debug("filling out email field")
        page.sign_in_page.fill_out_email_field(test_data['email'])
        self.logger.debug("filling out password field")
        page.sign_in_page.fill_out_password_field(test_data['password'])
        self.logger.debug("clicking submit button")
        page.sign_in_page.click_submit_button()

        self.logger.debug("getting snack message")
        actual_auth_failed_snack_text = page.sign_in_page.get_auth_failed_snack_text()
        self.logger.debug("asserting snack message")
        assert 'Authentication failed. User not found or password does not match' in actual_auth_failed_snack_text
        # this will assert user failed to log in based on url
        self.logger.debug("asserting user is not logged in")
        assert page.sign_in_page.page_url in driver.current_url

    #  student sign in with valid credentials
    def test_sign_in_student_positive(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        page = CommonPage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('web', 'TestSignIn', 'sign_in_student_positive')

        self.logger.debug(f"navigating to url: {config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        driver.get(f"{config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        self.logger.debug("filling out email field")
        page.sign_in_page.fill_out_email_field(test_data['email'])
        self.logger.debug("filling out password field")
        page.sign_in_page.fill_out_password_field(test_data['password'])
        self.logger.debug("clicking submit button")
        page.sign_in_page.click_submit_button()

        self.logger.debug("getting user name")
        actual_user_name = page.homepage.get_user_name_text()
        self.logger.debug("getting user role")
        actual_user_role = page.homepage.get_user_role_text()
        self.logger.debug("asserting user role")
        assert actual_user_role == 'STUDENT'
        self.logger.debug("asserting user name")
        assert actual_user_name == 'Student One'

    #  student sign in with invalid credentials
    def test_sign_in_student_negative(self, setup):
        self.logger.debug("invoking browser")
        driver = setup
        page = CommonPage(driver)
        self.logger.debug("getting test data")
        test_data = get_test_data('web', 'TestSignIn', 'sign_in_student_negative')

        self.logger.debug(f"navigating to url: {config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        driver.get(f"{config.get()['WEB']['base_url']}{page.sign_in_page.page_url}")
        self.logger.debug("filling out email field")
        page.sign_in_page.fill_out_email_field(test_data['email'])
        self.logger.debug("filling out password field")
        page.sign_in_page.fill_out_password_field(test_data['password'])
        self.logger.debug("clicking submit button")
        page.sign_in_page.click_submit_button()

        self.logger.debug("getting snack message")
        actual_auth_failed_snack_text = page.sign_in_page.get_auth_failed_snack_text()
        self.logger.debug("asserting snack message")
        assert 'Authentication failed. User not found or password does not match' in actual_auth_failed_snack_text

        self.logger.debug("asserting user is not logged in")
        assert page.sign_in_page.page_url in driver.current_url

import db.q_quiz as db_quiz
from api.register_student import register_student_account
from api.quiz import *
from api.delete_user import delete_account
from api.activate import activate_account
from api.sign_in import sign_in
from utilities.logger import get_logger as log
from utilities.test_data import get_test_data
import pytest

@pytest.mark.quiz
class TestApiQuiz:
    logger = log()

    @pytest.mark.skip
    def test_api_db_quiz_create(self, setup):
        # get token from response generated by setup fixture
        token = setup.json().get("token")
        # api call to create quiz and get id, override attribute value
        pytest.quiz_id = create_quiz(token).json().get('id')
        assert pytest.quiz_id == db_quiz.get_quiz_record_by_id(pytest.quiz_id)[0].get('id')  # verify
        # presence of created quiz in db

    @pytest.mark.regression
    def test_api_quiz_get(self, setup):
        """
        Test for endpoint /quizzes, validating key-value pairs in json response object
        """
        self.logger.debug("test_api_quiz_get : getting authentication token")
        token = setup.json().get("token")  # get token from response generated by setup fixture
        self.logger.debug("test_api_quiz_get : getting list of quizzes/asserting response status code")
        response = get_quizzes(token)
        self.logger.debug("test_api_quiz_get : asserting response code")
        assert response.status_code == 200
        self.logger.debug("test_api_quiz_get : asserting response time <=500ms")
        assert response.elapsed.total_seconds() <= 0.5
        quiz_list = response.json()
        for quiz in quiz_list:
            self.logger.debug(f"test_api_quiz_get : asserting key-values of quiz id = {quiz['id']}")
            assert isinstance(quiz['name'], str), "name value must be string"
            assert isinstance(quiz['questions'], list), "questions value must be list"
            assert isinstance(quiz['totalScore'], int), "totalScore value must be int"
            assert isinstance(quiz['passingPercentage'], int), "passingPercentage value must be int"
            assert isinstance(quiz['showStopperQuestion'], int) or quiz[
                'showStopperQuestion'] is None, "showStopperQuestion value must be int or None"
            assert isinstance(quiz['id'], int), "id value must be int"
            assert isinstance(quiz['createdAt'], str), "createdAt value must be str"
            assert isinstance(quiz['updatedAt'], str), "updatedAt value must be str"


# Test suit for endpoint /sign up, validating allowed values for email in request json object
@pytest.mark.regression
class TestApiRegistrationEmail:
    logger = log()

    def test_allowable_chars_alpha_special(self):
        """
         Positive, Allowable characters: Alphanumeric & Special characters
        """
        self.logger.debug("test_allowable_chars_alpha_special : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'positive1'))
        self.logger.debug("test_allowable_chars_alpha_special : asserting response status code")
        assert response.status_code == 200


    def test_empty_email_field(self):
        """
        Negative, Email field required, can’t be empty
        """
        self.logger.debug("test_empty_email_field : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative1'))
        self.logger.debug("test_empty_email_field : asserting response status code")
        assert response.status_code == 420

    def test_max_char_128(self):
        """
        Positive, Max 128 characters (128)
        """
        self.logger.debug("test_max_char_128 : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'positive2'))
        self.logger.debug("test_max_char_128 : asserting response status code")
        assert response.status_code == 200

    def test_max_char_129(self):
        """
        Negative, Max 128 characters (129)
        """
        self.logger.debug("test_max_char_129 : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative2'))
        self.logger.debug("test_max_char_129 : asserting response status code")
        assert response.status_code == 500

    def test_local_port_spaces(self):
        """
        Negative, White spaces are not allowed (local port)
        """
        self.logger.debug("test_local_port_spaces : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative3'))
        self.logger.debug("test_local_port_spaces : asserting response status code")
        assert response.status_code == 500

    def test_domain_spaces(self):
        """
        Negative, White spaces are not allowed (domain)
        """
        self.logger.debug("test_domain_spaces : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative4'))
        self.logger.debug("test_domain_spaces : asserting response status code")
        assert response.status_code == 500

    # Known bug
    # Negative, White spaces are not allowed (last part of the domain)
    @pytest.mark.skip
    def test_last_part_domain_spaces(self):
        self.logger.debug("sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative5'))
        self.logger.debug("asserting response status code")
        assert response.status_code == 500


    def test_local_port_64_char(self):
        """
        Positive, Local port with 64 characters (64)
        """
        self.logger.debug("test_local_port_64_char : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'positive3'))
        self.logger.debug("test_local_port_64_char : asserting response status code")
        assert response.status_code == 200

    # Known bug
    # Negative, Local port with 64 characters (65)
    @pytest.mark.skip
    def test_local_port_65_char(self):
        self.logger.debug("sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative6'))
        self.logger.debug("asserting response status code")
        assert response.status_code == 500

    def test_domain_right_63_char(self):
        """
        Positive, Domain on the right with 63 characters (63)
        """
        self.logger.debug("test_domain_right_63_char : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'positive4'))
        self.logger.debug("test_domain_right_63_char : asserting response status code")
        assert response.status_code == 200

    # Known bug
    # Negative, Domain on the right with 63 characters (64)
    @pytest.mark.skip
    def test_domain_right_64_char(self):
        self.logger.debug("sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative7'))
        self.logger.debug("asserting response status code")
        assert response.status_code == 500

    def test_domain_last_63_char(self):
        """
        Positive, characters in the last part of the domain (63)
        """
        self.logger.debug("test_domain_last_63_char : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'positive5'))
        self.logger.debug("test_domain_last_63_char : asserting response status code")
        assert response.status_code == 200

    # Known bug
    # Negative, 63 characters in the last part of the domain (64)
    @pytest.mark.skip
    def test_domain_last_64_char(self):
        self.logger.debug("sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative8'))
        self.logger.debug("asserting response status code")
        assert response.status_code == 500

    # Known bug
    # Negative, should contain top level domain separated by dot
    @pytest.mark.skip
    def test_tld_separated_dot(self):
        self.logger.debug("sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative9'))
        self.logger.debug("asserting response status code")
        assert response.status_code == 500

    def test_at_sign(self):
        """
        Negative, No @ sign
        """
        self.logger.debug("test_at_sign : sending request to register user and saving response")
        response = register_student_account(get_test_data('api', 'TestRegistrationEmail', 'negative10'))
        self.logger.debug("test_at_sign : asserting response status code")
        assert response.status_code == 500


# End-to-end test suit for API
@pytest.mark.regression
class TestE2E:
    logger = log()

    def test_e2e_student_regi_activ_sign_in(self, setup):
        """
        Test for student registration, activation and sign in
        """
        # test data will be used to create new student user
        test_data = get_test_data('api', 'TestE2E', 'student_regi_activ_sign_in')
        self.logger.debug("test_e2e_student_regi_activ_sign_in : sending request to register student user")
        response = register_student_account(test_data)
        self.logger.debug("test_e2e_student_regi_activ_sign_in : asserting status code 200")
        assert response.status_code == 200
        self.logger.debug("test_e2e_student_regi_activ_sign_in : activating account")
        activate_account(test_data["email"])
        self.logger.debug("test_e2e_student_regi_activ_sign_in : sending request to sign in activated user")
        response = sign_in(test_data["email"], test_data["password"])
        self.logger.debug("test_e2e_student_regi_activ_sign_in : asserting status code 200")
        assert response.status_code == 200
        self.logger.debug("test_e2e_student_regi_activ_sign_in : deleting user")
        response = delete_account(test_data['email'], setup.json()['token'])
        if response.status_code == 200:
            self.logger.debug("test_e2e_student_regi_activ_sign_in : user deleted")
        else:
            self.logger.error(f"test_e2e_student_regi_activ_sign_in : user is not deleted, server response code: {response.status_code}, body: {response.json()}")



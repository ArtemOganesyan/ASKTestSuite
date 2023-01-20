import db.q_users as db_tests
from api.register_student import register_student_account

class TestSample:
    def test_db_user_exist(self):
        assert db_tests.user_exist("raha.fake@gmail.com")[0]['id'] > 0

    def test_api_registration(self):
        response = register_student_account()
        assert response.status_code == 200
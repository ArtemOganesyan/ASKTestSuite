from utilities import db


def get_quiz_record_by_id(q_id):
    return db.query(f'select * from quizzes where id = {q_id}')


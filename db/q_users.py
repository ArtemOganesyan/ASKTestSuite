from utilities import db

def user_exist(email):
    return db.query(f'select id from users where email="{email}";')
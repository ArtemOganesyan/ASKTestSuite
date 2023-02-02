import json
import requests as requests
from api.sign_in import sign_in
import config
from utilities import db


def delete_account(email, token):
    # send query to id by email and store it in a list
    user_data = db.query(f'select id from users where email = "{email}"')
    # send api request with id to delete user
    url = f"{config.get()['API']['base_url']}/users/{user_data[0].get('id')}"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.request("DELETE", url, headers=headers)
    return response







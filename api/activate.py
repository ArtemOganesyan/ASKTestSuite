import json
import requests as requests
import config
from utilities import db


def activate_account(email):
    # send query to retrieve activation code and id by email and store it in a list
    user_data = db.query(f'select id, activationCode from users where email = "{email}"')
    # send api request with id and activation code to activate user
    url = f"{config.get()['API']['base_url']}/activate/{user_data[0].get('id')}/{user_data[0].get('activationCode')}"
    response = requests.request("GET", url)
    return response








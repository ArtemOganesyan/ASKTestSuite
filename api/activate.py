import json
import requests as requests
import config
from utilities import db


def activate_account(email):
    user_data = db.query(f'select id, activationCode from users where email = "{email}"')  # query id, activationCode,
    # store in a list
    url = f"{config.get()['API']['base_url']}/activate/{user_data[0].get('id')}/{user_data[0].get('activationCode')}" #  pass
    # id and activation code as path params

    response = requests.request("GET", url)
    return response








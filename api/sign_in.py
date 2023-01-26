import json
import requests as requests
import config


def sign_in():
    url = f"{config.get()['API']['base_url']}/sign-in"
    payload = json.dumps({
        "email": config.get()["TEST_USERS"]["teacher_email"],
        "password": config.get()["TEST_USERS"]["teacher_password"],
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


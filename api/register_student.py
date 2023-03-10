import json
import requests as requests
import config


def register_student_account(test_data):
    url = f"{config.get()['API']['base_url']}/sign-up"
    payload = json.dumps(test_data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

import pytest
import config
import json
import requests as requests


#  fixture script executes API sign in call and returns response object to test method
@pytest.fixture
def setup():
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

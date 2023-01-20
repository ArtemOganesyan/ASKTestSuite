import json
import requests as requests
import config


def register_student_account():
  url = f"{config.get()['API']['base_url']}/sign-up"
  payload = json.dumps({
    "email": "api_test_user@gmail.com",
    "password": "12345Abc",
    "name": "Test User",
    "group": "ABC111"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return response
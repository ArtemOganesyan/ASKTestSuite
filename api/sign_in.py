import json
import requests as requests
import config


def sign_in():
  url = f"{config.get()['API']['base_url']}/sign-in"
  payload = json.dumps({
    "email": "api_test_user@gmail.com",
    "password": "12345Abc",
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return response


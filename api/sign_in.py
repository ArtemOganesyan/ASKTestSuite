import json
import requests as requests
import config


def sign_in(email, password):
    url = f"{config.get()['API']['base_url']}/sign-in"
    payload = json.dumps({"email": email,
                          "password": password
                          })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


sign_in('student1@gmail.com','student12345')
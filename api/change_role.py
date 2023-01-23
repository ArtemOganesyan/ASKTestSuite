import json
import requests as requests
import config
from utilities import db
import sign_in

# test is not fully functional 

def change_role(email, new_role):
    user_data = db.query(f'select id from users where email = "{email}"')  # query id, activationCode,
    # store in a list
    print(user_data)
    url = f"{config.get()['API']['base_url']}/users/change-role/{user_data[0].get('id')}"

    headers = {
        "Content=type": "application/json",
        "Authentication": f"Bearer {sign_in.sign_in().json().get('token')}"
    }

    payload = json.dumps({
        "role": new_role
    })

    response = requests.request("GET", url, headers=headers, data=payload)
    return response







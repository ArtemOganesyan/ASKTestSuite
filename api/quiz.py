import json
import requests as requests
import config
from api import sign_in


def create_quiz(token):
    url = f"{config.get()['API']['base_url']}/quiz"
    payload = json.dumps({
        "id": False,
        "name": "Api_test_python",
        "totalScore": 10,
        "passingPercentage": 75,
        "showStopperQuestion": 0,
        "questions": [{"type": "SINGLE_CHOICE", "question": "Color of sea", "score": 5, "options": ["blue", "red"],
                       "answer": 0, "hasOtherOption": False},
                      {"type": "SINGLE_CHOICE",
                       "question": "Color of forest",
                       "score": 5,
                       "options": ["green", "red"]
                          , "answer": 0,
                       "hasOtherOption": False}],
        "createdAt": False, "updatedAt": False
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'  # call sign in function to sign in
        # with teacher permissions and get authorisation token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response


# token = sign_in.sign_in().json().get("token")

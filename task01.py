import requests
import json

url = "https://randomuser.me/api/?gender=female"

jsonfile = requests.get(url)
file = jsonfile.json()

user = file['results'][0]

user_dict = {
    "first_name": user['name']['first'],
    "last_name": user['name']['last'],
    "gender": user['gender'],
    "email": user['email'],
    "phone": user['phone'],
    "address": {
        "street": f"{user['location']['street']['number']} {user['location']['street']['name']}",
        "city": user['location']['city'],
        "country": user['location']['country']
    }
}

with open("jsonfile/user.json", "w", encoding="utf-8") as f:
    json.dump(user_dict, f, indent=4)
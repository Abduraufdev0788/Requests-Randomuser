import requests
import json

url = "https://randomuser.me/api/?results=20"
response = requests.get(url).json()
save_json = list()

for user in response['results']:
    if user['dob']['date'][:4] > "1990" :
        user_dict = {
            "name": user['name']['first'],
            "brith_year":user['dob']['date'][:4],
            "email":user['email']
        }
        save_json.append(user_dict)
    
with open("jsonfile/young_users.json", "w") as jsonf:
    json.dump(save_json,jsonf, indent=4, ensure_ascii=False)
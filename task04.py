import requests
import json

url = "https://randomuser.me/api/?results=10"
respons = requests.get(url).json()
save = list()

for user in respons['results']:
    user_dict = {
        "full name": user['name']['first']+ " " + user['name']['last'],
        "email": user['email'],
        "picture.large":user['picture']['large']
    }
    save.append(user_dict)
with open("jsonfile/users_with_images.json", "w") as jsonfile :
    json.dump(save, jsonfile, indent=4, ensure_ascii=False)

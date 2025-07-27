import requests
import json

url = "https://randomuser.me/api/?results=10"

response = requests.get(url)
users = response.json()
result = users['results']
save_Users = []

for results in result:
    user_dict = {
        "full_name" : results['name']['first'] +" " + results['name']['last'],
        "email": results['email'],
        "gender": results['gender'],
        "country": results['location']['country']
    }
    save_Users.append(user_dict)
with open("jsonfile/users.json", "w") as file:
    json.dump(save_Users,file, indent=4, ensure_ascii=False)

import csv
import requests

url = 'https://randomuser.me/api/?results=10'
responce = requests.get(url)
data = responce.json()

with open("users.csv", "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ['full_name', 'gender', 'email', 'phone', 'country']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()


    for user in data['results']:
        full_name = f"{user['name']['first']} {user['name']['last']}"
        gender = ['gender']
        email = user['email']
        phone = user['phone']
        country = user['location']['country']

        writer.writerow({
            'full_name' : full_name,
            'gender' : gender,
            'email' : email,
            'phone' : phone,
            'country' : country
        })



print("csv ga yozildi")
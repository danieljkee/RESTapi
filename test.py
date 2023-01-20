import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "HUY", "views": 1245, "likes": 100},
        {"name": "PIZDA", "views": 6969, "likes": 1119},
        {"name": "SISKI", "views": 6666, "likes": 696}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + "video/6")
print(response.json())


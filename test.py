import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "HUY", "views": 1245, "likes": 100},
        {"name": "PIZDA", "views": 6969, "likes": 1119},
        {"name": "SISKI", "views": 6666, "likes": 696}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())

# response = requests.put(BASE + "video/1", {"name": "HUY", "views": 1245, "likes": 10})
# response = requests.put(BASE + "video/1", {"name": "HUY", "views": 1245, "likes": 10})
# print()
# response = requests.get(BASE + "video/1")
# response = requests.delete(BASE + "video/1")

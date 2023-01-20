import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"name": "HUY", "views": 1245, "likes": 100},
#         {"name": "PIZDA", "views": 6969, "likes": 1119},
#         {"name": "SISKI", "views": 6666, "likes": 696}]
#
# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())
# response = requests.put(BASE + "video/3", {"name": "PIPISKI", "views": 12345, "likes": 123})
# response = requests.put(BASE + "video/3", {"name": "PIPISKI", "views": 12345, "likes": 123})
# for i in range(5):
#     response = requests.get(BASE + "video/" + str(i))
#     print(response.json())
# # response = requests.get(BASE + "video/0")
#
#
# response = requests.put(BASE + "video/4", {"name": "SSS", "views": 333, "likes": 333})
# for i in range(5):
#     response = requests.get(BASE + "video/" + str(i))
#     print(response.json())
# response = requests.delete(BASE + "video/4")
# for i in range(5):
#     response = requests.get(BASE + "video/" + str(i))
#     print(response.json())
response = requests.delete(BASE + "video/4")
print(response.json())
# response = requests.patch(BASE + "video/2", {"likes": 999, "views": 3333})
# print(response.json())

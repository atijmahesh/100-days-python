import requests
from datetime import datetime
USERNAME = "atijmahesh"
TOKEN  = "kasf8sdjfklajlc"
GRAPH_NAME = "graph1"

pixel_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}
#user creation
# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_NAME,
    "name": "Workout Graph",
    "unit": "minutes",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# #post pixel today
# today = datetime.now()

# endpoint = f"{graph_endpoint}/{GRAPH_NAME}"
# pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "65.5",
# }
# response = requests.post(url=endpoint, json=pixel_config, headers=headers)
# print(response.text)

# #post pixel yesterday
# today = datetime(year=2024, month=8,day=3)

# endpoint = f"{graph_endpoint}/{GRAPH_NAME}"
# pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "12.5",
# }
# response = requests.post(url=endpoint, json=pixel_config, headers=headers)
# print(response.text)


#update pixel from yesterday
today = datetime(year=2024, month=8,day=3)

endpoint = f"{graph_endpoint}/{GRAPH_NAME}"
new_pixel_data = {
    "quantity": "245.3"
}
update_endpoint = f"{endpoint}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

#delete yesterdays
r = requests.delete(url=update_endpoint, headers=headers)
print(r)
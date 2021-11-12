import requests
from datetime import datetime

TOKEN = "hrjpsjgzkldgkzhrehlkhrehr382"
USERNAME = "saswati"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "int",
    "color": "shibafu"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_creation_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many chapters did you study today? "),
}

update_pixel_creation_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_config, headers=headers)
print(response.text)

new_pixel_data = {
    "quantity": "3",
}

# response = requests.put(url=update_pixel_creation_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

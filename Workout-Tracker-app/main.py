import requests


GENDER = "female"
WEIGHT_KG = 59
HEIGHT_CM = 172
AGE = 30
APP_ID = "1ca0eac6"
API_KEY = "b6ecb996fc7a3abb2681d38ed8e92f50"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)

result = response.json()
print(result)
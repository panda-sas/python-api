import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "e8b69cf3e135668787d23c2c78fe52da"
account_sid = "AC14aa67dd5720e3a08ba9931b82cc2352"
auth_token = 'ab9398d4b007c9c2e4efaf5d51177d4d'

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

will_rain = False

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body ="It's going to rain today. Remember to bring an umbrella ☔",
        from_="+17176475903",
        to ="+15122101474"
    )
    print(message.status)

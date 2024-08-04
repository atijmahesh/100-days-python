import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
MY_LAT = "40.3060"
MY_LONG = "121.0058"
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()["list"]
forecast_list = [entry["weather"][0]["id"] for entry in weather_data]
will_rain = False
for forecast in forecast_list:
    if forecast < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_="whatsapp:+14155238886",
        to="whatsapp:+14086181185",
    )

    print(message.status)

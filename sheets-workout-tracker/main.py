import requests
from datetime import datetime

APP_ID = "2d067b36"
API_KEY = "4b61322422db8431399e3745ac3c9297"
DOMAIN = "https://trackapi.nutritionix.com"
workout_endpoint = f"{DOMAIN}/v2/natural/exercise"
sheets_endpoint = "https://api.sheety.co/cdb3100131e7b4d0f2171fdbf9792030/pythonWorkoutTracker/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

resp = input("Tell me which exercises you did: ")
workout_params = {
    "query": resp
}

r = requests.post(url=workout_endpoint, json=workout_params, headers=headers)
result = r.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheets_endpoint, json=sheet_inputs)

    print(sheet_response.text)

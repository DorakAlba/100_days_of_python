import requests
import datetime as dt
import os
exercise_endpoint = input('What you did? ')
sheety_endpoint = 'https://api.sheety.co/888188e34cf00cfe406cfdb85af894be/workoutTracking/workouts'

APP_ID = os.environ.get('APP_ID')
API_KEY = 'API_KE'
GENDER = 'male'
WEIGHT_KG = '76'
HEIGHT_CM = '193'
head = {"Authorization":'Bearer xxxxx'}

headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
    'x-remote-user-id': '0'
}
call = {
    'query' : exercise_endpoint,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}
to_post = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise = requests.post(url = to_post,json = call, headers=headers)
ex = exercise.json()
for value in ex['exercises']:
    activity = value['user_input']
    duration = value['duration_min']
    calories = value['nf_calories']
    dates = dt.datetime.now()
    date = dates.strftime('%d/%m/%Y')
    time = dates.strftime('%H:%M:%S')
    result ={'workout' : {'date':date,
               'time':time,
               'exercise':activity,
               'duration':duration,
               "calories":calories
    }}
    exercise_post = requests.post(url = sheety_endpoint, json=result, headers = head)
    exercise_post.raise_for_status()

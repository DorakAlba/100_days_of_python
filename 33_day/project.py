import requests
from datetime import datetime
import smtplib
import threading
my_mail = ''
my_pass = ''
MY_LAT = 55.749931 # Your latitude
MY_LONG = 48.742371 # Your longitude
print('hah')
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def satelite():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if abs(iss_latitude - MY_LAT) <5 and abs(iss_longitude - MY_LONG)<5:
        if time_now.hour< sunrise or time_now.hour > sunset:
            smt = smtplib.SMTP(host='smtp.mail.yahoo.com',port = 587)
            smt.starttls()
            smt.login(user = my_mail, password=my_pass)
            smt.sendmail(my_mail,'mr.demyank@gmail.com','Subject:look above \n\n You can see satelite!')
            threading.Timer(60, satelite)
        satelite()
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.




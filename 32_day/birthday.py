##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas as pd
import os, random

email =''
password =''
data = pd.read_csv('birthdays.csv')
today = dt.datetime.now()
for index,row in data.iterrows():
    if row['month'] == today.month and row['day'] == today.day:
        letter = random.choice(os.listdir('letters'))
        with open(f"letters\{letter}",'r') as let:
            message = let.read()
        message = message.replace("[NAME]",row['name'])
        print(message)
        with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
            connection.starttls()
            connection.login(user = email, password= password)
            connection.sendmail(email, row['email'], msg=f"Subject:Happy Birthday! \n\n{message} ")






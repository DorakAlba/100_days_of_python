import smtplib
# 
my_email =
send_to =
my_password =
# with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
    # connection.sendmail(from_addr=my_email, to_addrs=send_to, msg='Subject:My_body \n\nThis is content')
# 

import datetime as dt
import random as rd
now = dt.datetime.now()
bd_date = dt.datetime(year = 1995, month = 11, day = 12)
print(now.year)

day_of_week = now.weekday()
print(day_of_week)
with open('quotes.txt','r') as text:
    document = text.readlines()
print (document[0])
if day_of_week == 0:
    quote = rd.choice(document)
    with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=send_to, msg=f'Subject:Today Quote \n\n{quote}')


import os
with open('last_day.txt') as day:
    text = int(day.read())+1

os.mkdir (f'{text}_day')
with open(f"{text}_day/main.py",'w') as g:
    g.write('')
with open('last_day.txt','w') as day:
    day.write(str(text))

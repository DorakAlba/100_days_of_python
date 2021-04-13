import random as rd
from tkinter import *
import json
import pandas as pd
import random as rd
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
word_pair = None
# ------------- Data Loading -----------#
# try:
#     with open('french_tried.json') as a:
#         text = json.load(a)
# except FileNotFoundError:
#     data = pd.read_csv('french_words.csv')
#     data.to_json(orient='records')
#     with open('french_tried.json','w') as a:
#         text = json.load(a)

try:
    data = pd.read_csv('words_to_learn.csv')
    if  data.empty:
        data = pd.read_csv('french_words.csv')
except:
    data = pd.read_csv('french_words.csv')
text = data.to_dict(orient = 'records')
# text = text.to_dict(orient='records')
word = {}
# ----------- Functions ---------------#
def next_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_back, image = pic_canvas)
    canvas.itemconfig(card_title, text='French', fill = 'black')
    word = rd.choice(text)
    canvas.itemconfig(card_text, text=word['French'],fill='black')
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(card_back, image = pic_canvas_back)
    canvas.itemconfig(card_title, text='English',fill='white')
    canvas.itemconfig(card_text, text= word['English'],fill='white')


def is_know():
    try:
        text.remove(word)
        data = pd.DataFrame(text)
        data.to_csv('words_to_learn.csv',index=False)

        next_word()
    except IndexError:
        messagebox.showinfo(text= 'No More Cards Left', title='Well Done')


# ---------------- UI -------------------#
window = Tk()
window.title('Flashed')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func = flip_card)
# picture
pic_yes = PhotoImage(file="images/right.png")
pic_no = PhotoImage(file="images/wrong.png")
pic_canvas = PhotoImage(file="images/card_front.png")
pic_canvas_back = PhotoImage(file="images/card_back.png")
# windows
canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = canvas.create_image(400, 263, image=pic_canvas)
canvas.grid(column=0, row=0, columnspan=2)
# buttons
button_accept = Button(image=pic_yes, command=is_know)
button_accept.grid(row=2, column=1)
button_forgot = Button(image=pic_no, command=next_word)
button_forgot.grid(row=2, column=0)
# labels
card_title = canvas.create_text(400, 150, text="Title", font=('Ariel', 40, 'italic'))
card_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
# button_forgot =

next_word()
window.mainloop()

# ------------- Launch -----------------#

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list2 = [random.choice(numbers) for _ in range(nr_symbols)]
    password_list3 = [random.choice(symbols) for _ in range(nr_numbers)]
    password_list.extend(password_list2)
    password_list.extend(password_list3)


    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def accepted():
    t1 = web_entry.get()
    t2 = email_entry.get()
    t3 = password_entry.get()
    is_ok = messagebox.askokcancel(title=t1,
                                   message=f'Details entered page: {t1}, email: {t2}, password: {t3}\n is it ok to save? ')
    if is_ok:
        if t1 == "" or t3 == "":
            messagebox.showinfo(message = "Don't leave this stuff empty")
        else:
            with open('data.txt', 'a') as g:
                g.write(f"\n{t1} | {t2} | {t3}")
            web_entry.delete(0, END)
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text='Website:', font=('Courier', 10, 'bold'))
website.grid(column=0, row=1)

email = Label(text='Email/Username:', font=('Courier', 10, 'bold'))
email.grid(column=0, row=2)
password = Label(text='Password:', font=('Courier', 10, 'bold'))
password.grid(column=0, row=3)
generate_pass = Button(text='Generate Password', font=('Courier', 10, 'bold'),command=gen_pass)
generate_pass.grid(column=2, row=3)

add_text = Button(text='Add', font=('Courier', 10, 'bold'), width=40, command=accepted)
add_text.grid(column=1, row=4, columnspan=2)

web_entry = Entry(width=46)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=46)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, 'dogmail@hotdog.com')
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
window.mainloop()

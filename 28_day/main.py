from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    done_label.config(text = '')
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text =  "00:00")
    it_timer.config(text='Timer😃')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps  in [1,3,5,7]:
        it_timer.config(text="Focus!👌", fg=RED)
        count_down(25*60)
        reps+=1
    elif reps  in [2,4,6]:
        it_timer.config(text="Rest!",fg=PINK)
        count_down(60*5)
        reps +=1
        done_label.config(text = (u'\u2713'*(int(reps/2))))
    else:
        it_timer.config(text="Big Rest❤", fg=GREEN)
        count_down(20*60)
        reps=1
        done_label.config(text = (u'\u2713'*(int(reps/2))))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = count%60
    if len(str(minutes))<2:
        minutes = '0'+str(minutes)
    canvas.itemconfig(timer_text, text =  f"{int(count / 60)}:{minutes}")
    if count>0:
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Tomato')
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=250, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(125, 112, image=tomato_img)
timer_text = canvas.create_text(125, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Name
it_timer = Label(text='Timer😃', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
it_timer.grid(column=1, row=0)
button_start = Button(text='Start', width=6, height=1,highlightthickness=0)
button_start.grid(column=0, row=3)
button_reset = Button(text='Reset', width=6 , height=1,highlightthickness=0)
button_reset.grid(column=3, row=3)
# Label
done_label = Label(fg= GREEN, bg = YELLOW)
done_label.grid  (column = 1, row=3)

button_start.config(command = start_timer)
button_reset.config(command = reset)


window.mainloop()



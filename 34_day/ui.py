from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # self.window.padding()
        self.score = Label(text=f"Score : {self.quiz.score}", font=('Arial', 14, 'italic'), bg=THEME_COLOR, fg='white')
        img_y = PhotoImage(file='true.png')
        img_n = PhotoImage(file='false.png')
        self.yes = Button(image=img_y,command = self.yes_answer)
        self.no = Button(image=img_n, command = self.no_answer)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,width = 280, text='Question', font=("Arial", 20, 'italic'))

        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.yes.grid(column=0, row=2)
        self.no.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = 'Its end of the quiz')
            self.yes.config(state='disabled')
            self.no.config(state='disabled')
    def yes_answer(self):
        result = self.quiz.check_answer('true')

        self.feedback(result)
    def no_answer(self):
        result = self.quiz.check_answer('false')
        self.feedback(result)

    def feedback(self,result):
        if result:
            self.canvas.config(bg = 'green')
            self.score.config(text = f"Score : {self.quiz.score}")
        else:
            self.canvas.config(bg = 'red')

        self.window.after(1000, self.next_question)

    def next_question(self):
        self.get_next_question()
        self.canvas.config(bg='white')


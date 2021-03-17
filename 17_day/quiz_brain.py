import random


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        print(f"question № {self.question_number + 1} : {question.text}")
        answer = input("true/false: ").lower()
        self.question_number += 1
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, true_answer):
        if answer == true_answer.lower():
            print('you right')
            self.score += 1
        else:
            print(f"you wrong, answer was {true_answer} ")
        print(f"you'r score {self.score / self.question_number}")

    def still_have_question(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True

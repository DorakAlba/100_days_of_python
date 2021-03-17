from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question = []
for entry in question_data:
    question.append(Question(entry['text'], entry['answer']))

quiz = QuizBrain(question)
quiz.next_question()

while quiz.still_have_question():
    quiz.next_question()
print('you completed the quiz')
print (f" you score self{quiz.score/quiz.question_number}")
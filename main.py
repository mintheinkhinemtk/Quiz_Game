from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q = Question(item['text'],item['answer']) # q means 'question'
    question_bank.append(q)

#print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz!\nYour final score was {quiz.score}/{quiz.ques_num}")
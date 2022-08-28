from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank_text = question_data[i]["question"]
    question_bank_answer = question_data[i]["correct_answer"]
    question_bank.append(Question(question_bank_text,question_bank_answer ))
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
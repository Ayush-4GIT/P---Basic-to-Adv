
from Datasets.Day_17.question_model import Question
from Datasets.Day_17.data import question_data
from Datasets.Day_17.quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
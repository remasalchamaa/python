from data import question_bank
from quiz import Question

question_bank_obj = [Question(question["question"], question["correct_answer"]) for question in question_bank]
score = 0 
for i, question in enumerate(question_bank_obj):
    answer = input(f"Q:{i+1}/{len(question_bank_obj)}: {question.question} (True/False):")
    if answer.lower() == question.answer.lower():
        score += 1
        print(f"Correct! Your score is {score}/{i+1}")
    else:
        print(f"Incorrect! Your score is {score}/{i+1}")

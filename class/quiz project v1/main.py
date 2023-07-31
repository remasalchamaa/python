from data import question_bank
from quiz import TestTaker, Question

question_bank_obj = [Question(question["question"], question["correct_answer"]) for question in question_bank]
test_taker = TestTaker(question_bank_obj)

while test_taker.has_next():
    test_taker.next_question()

class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class TestTaker():
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.score = 0
        self.question_number = 0

    def next_question(self):
        next_question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number}/{len(self.question_bank)}: {next_question.question} (True/False):")
        
        if user_answer.lower() == next_question.answer.lower():
            self.score += 1
            print(f"Correct! Your score is {self.score}/{self.question_number}")
        else:
            print(f"Incorrect! Your score is {self.score}/{self.question_number}")

    def has_next(self):
        return self.question_number < len(self.question_bank)
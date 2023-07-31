class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    


class Quiz():
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.n_questions = len(question_bank)

    def start(self):
        self.question_number = 0
        self.score = 0
        
        while self.question_number < self.n_questions:
            self.next_question()
            self.question_number += 1

    def next_question(self):
        question = self.question_bank[self.question_number]
        self.question_text = question["question"]
        self.question_answer = question["correct_answer"]
        self.ask_question()

    def ask_question(self):
        self.answer = input(f"Q.{self.question_number+1}/{self.n_questions}: {self.question_text} (True/False): ")
        eval = self.check_answer()
        if eval==True:
            self.score += 1
            print(f"Correct! Your score is {self.score}/{self.question_number+1}")
        else:
            print(f"Incorrect! Your score is {self.score}/{self.question_number+1}")

    def check_answer(self):
        if self.answer.lower() == self.question_answer.lower():
            return True
        else:
            return False
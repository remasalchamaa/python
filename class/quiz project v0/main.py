from data import question_bank

score = 0 
for i, question in enumerate(question_bank):
    answer = input(f"Q:{i+1}/{len(question_bank)}: {question['question']} (True/False):")
    if answer.lower() == question['correct_answer'].lower():
        score += 1
        print(f"Correct! Your score is {score}/{i+1}")
    else:
        print(f"Incorrect! Your score is {score}/{i+1}")

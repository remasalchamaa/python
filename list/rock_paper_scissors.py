import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
      
# create a list of rock, paper, scissors
rps = [rock, paper, scissors]

# get user input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(rps[user_choice])

# get computer input
computer_choice = random.randint(0, 2)
print("Computer chose:", computer_choice)
print(rps[computer_choice])

# determine winner
if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 1:
    print("You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win.")
elif user_choice == 1 and computer_choice == 0:
    print("You win.")
elif user_choice == 1 and computer_choice == 2:
    print("You lose.")
elif user_choice == 2 and computer_choice == 0:
    print("You lose.")
elif user_choice == 2 and computer_choice == 1:
    print("You win.")
else:
    print("You typed an invalid number. You lose.")



import random
#create a random number from 0, 1, 2
random_number = random.randint(0, 2)
print(random_number)

# create a random floating point 
random_float = random.random()
print(random_float)

# create a random floating point number between 2 and 5
random_float = random.random() * 3 + 2
print(random_float)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_right_m():
    turn_right()
    move()
    turn_right()


def turn_left_m():
    turn_left()
    move()
    turn_left()


turn_left()
for i in range(10):
    if i % 2 == 0:
        for j in range(9):
            move()
        turn_right_m()
    else:
        for j in range(9):
            move()
        if i != 9:
            turn_left_m()

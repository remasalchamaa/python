def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_step():
    while front_is_clear():
        if at_goal():
            return
        move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# method1
while not at_goal():
    one_step()

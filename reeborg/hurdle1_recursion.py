def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_step():
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
    one_step()
    # return one_step()


one_step()

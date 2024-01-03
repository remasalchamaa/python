def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_step():
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

# method2
# for _ in range(6):
#    one_step()

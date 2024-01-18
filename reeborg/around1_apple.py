i = 0 
while True:
    if front_is_clear():
        move()
    else:
        turn_left()
        i += 1
        if i == 4:
            break
    if object_here():
        take()

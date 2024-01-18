put()

while True:
    if front_is_clear():
        move()
    else:
        turn_left()
    
    if object_here():
        break
        

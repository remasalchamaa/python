def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_face_to_right():
    while not is_facing_north():
        turn_left()
    turn_right()

def turn_face_to_up():
    while not is_facing_north():
        turn_left()
    
def turn_face_to_left():
    while not is_facing_north():
        turn_left()
    turn_left()
    
def turn_face_to_down():
    while not is_facing_north():
        turn_left()
    turn_left()
    turn_left()
    
def maze(right=False, left=False, up=False, down=False):
    #print(right, left, up, down)
    if at_goal():
        done()

    if not left:
        turn_face_to_right()
        if front_is_clear():
            move()
            maze(right=True)
            
    if not down:
        turn_face_to_up()
        if front_is_clear():
            move()
            maze(up=True)
            
            
    if not right:
        turn_face_to_left()
        if front_is_clear():
            move()
            maze(left=True)
    
    if not up:
        turn_face_to_down()
        if front_is_clear():
            move()
            maze(down=True)
      
maze(False, False, False, False)
    

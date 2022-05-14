def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_left():
    int
def move():
    int   
def back_up():
    turn_left
    turn_left
    
def north():
    while not is_facing_north():
        turn_left()
north()
while not wall_in_front():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    if not wall_in_front():
        move()
    if not right_is_clear() and wall_in_front():
        back_up()
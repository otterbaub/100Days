def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def north():
    while not is_facing_north():
        turn_left()
north()
while not wall_in_front():
    move()
turn_left()
while not at_goal():
    while not wall_in_front():
        move()
    if at_goal():
            break
    if right_is_clear():
        turn_right()
        move()
    if not wall_on_right():
        turn_right()
        move()
    if wall_in_front() and right_is_clear():
        turn_left()
    if wall_in_front():
        turn_left()
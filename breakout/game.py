"""
Breakout game. Implemented using pygame. 

Bouncing and movement functions taken from this particle simulation: http://www.petercollingridge.co.uk/book/export/html/6.
"""

print("hello world")

import pygame
import math
import breakout
import constants

colors = [constants.RED, constants.ORANGE, constants.YELLOW]

""" 
Paddle: Methods
"""
# Update the position of the paddle. It is confined to the boundaries
# of the screen
def paddle_update_position(paddle):
    breakout.get_mouse_location()
    location = breakout.get_mouse_location()
    x_position = location[0]
    if x_position >= constants.SCREEN_WIDTH - constants.PADDLE_WIDTH - 5:
        x_position=constants.SCREEN_WIDTH - constants.PADDLE_WIDTH - 5

    breakout.set_x(paddle, x_position)


"""
Ball: Methods
"""

# This function must update the coordinates of the ball and changes the 
# direction of the ball bounces of either the left, top, or right walls 
def ball_update_position(ball):
    x = breakout.get_x(ball)
    y = breakout.get_y(ball)
    x_velocity = breakout.get_x_velocity(ball)
    y_velocity = breakout.get_y_velocity(ball)
    new_x = x + x_velocity
    new_y = y + y_velocity
    breakout.set_x(ball, new_x)
    breakout.set_y(ball, new_y)
    if new_x>= constants.SCREEN_WIDTH - constants.BALL_RADIUS:
        x_velocity = x_velocity *-1
    elif new_x<= constants.BALL_RADIUS:
        x_velocity = x_velocity *-1
    elif new_y <= constants.BALL_RADIUS:
        y_velocity = y_velocity*-1
    breakout.set_x_velocity(ball , x_velocity)
    breakout.set_y_velocity(ball , y_velocity)
    if new_y == constants.SCREEN_HEIGHT - constants.BALL_RADIUS:
        x_velocity = x_velocity
        y_velocity = y_velocity


    



    #TODO

# This function must change the direction of the ball when it hits an 
# object 
def ball_bounce_off(ball):
    y = breakout.get_y_velocity(ball)
    breakout.set_y_velocity (ball, y *-1)






"""
Screen Update: Methods
"""
# This function must render all objects on screen using breakout.py draw 
# methods. No objects should be created in this method. 
def draw_objects():
    breakout.clear_screen()

    # Draw the paddle, ball, and wall of bricks
    # TODO
    for brick in bricks:
        x = breakout.get_x(brick)
        y = breakout.get_y(brick)
        width = breakout.get_width(brick)
        height = breakout.get_height(brick)
        color = breakout.get_color(brick)
        breakout.draw_rectangle(x, y, width, height, color)
    x = breakout.get_x(paddle)
    y = breakout.get_y(paddle)
    width = breakout.get_width(paddle)
    height = breakout.get_height(paddle)
    color = breakout.get_color(paddle)
    breakout.draw_rectangle(x, y, width, height, color)
    
    x = breakout.get_x(ball)
    y = breakout.get_y(ball)
    radius = breakout.get_radius(ball)
    color = breakout.get_color(ball)
    breakout.draw_circle(x,y,radius, color)
    # Tell pygame to actually redraw everything (DON'T CHANGE)
    pygame.display.flip()


# This function must create the set of bricks to be drawn at the top of 
# the screen. 
# This function returns a list of bricks created. 
def build_bricks():
    # Create an empty list 
    bricks = []
    for s in range (6):
        y = s*25
        if s < 2:
            color = colors[0]
        elif s ==2:
            color = colors[1]
        elif s >=4:
            color = colors[2]
        for i in range(5):
            x = (i+1)*5 + i *75
            brick = breakout.create_new_brick()
            breakout.set_x(brick, x)
            breakout.set_y(brick, y)
            breakout.set_color(brick, color)
            bricks.append(brick)
    return bricks 

    # TODO 

    # Create the bricks and add them to list
    # Hint: You need a double for loop to draw the set of bricks on top of the screen. 
    # Set the brick color based on row number by using the colors in the constants.py
    # file. (You can add other colors if you wish). When you create a new brick and 
    # set the x,y, and color using breakout.py methods, add your brick to the list.
    # TODO 




# Creating the screen 
breakout.build_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

# Create the ball, paddle, and bricks here using breakout.py functions.

# TODO
bricks = build_bricks()
paddle = breakout.create_new_paddle()
ball = breakout.create_new_ball()


# These are variables used to detect the state of the game. 
running = True
start = False


while running:
    
    # Setup the mouse events 
    # DO NOT change this code
    for event in pygame.event.get():
        # If you click the mouse, the ball will start moving 
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = True 
        if event.type == pygame.QUIT:
            running = False

    paddle_update_position(paddle)
    if start == True:
        # Make the ball update its position. 
        ball_update_position(ball)
    if breakout.ball_did_collide_with(ball, paddle, constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT):
            ball_bounce_off(ball)
    for brick in bricks:
        if breakout.ball_did_collide_with(ball, brick, constants.BRICK_WIDTH, constants.BRICK_HEIGHT):
            ball_bounce_off(ball)
        if breakout.ball_did_collide_with(ball, brick, constants.BRICK_WIDTH, constants.BRICK_HEIGHT):
            bricks.remove(brick)



    if len(bricks) == 0:
        running = False 

       
    # Update the position of the paddle based on the mouse
    # TODO 
        
    # Check for collisions using breakout.ball_did_collide_with(ball, obj, width, height) 
    # TODO 

    y = breakout.get_y(ball)
    if y >= constants.SCREEN_HEIGHT - constants.BALL_RADIUS:
        running = False


    # TODO 

    # If bricks are all broken, you won! 

    # TODO 

    # Else, loop through the entire bricks list to see if the ball collided with any brick 
    # TODO 

    # Redraw everything at the end of the while loop

    draw_objects()

pygame.display.update()

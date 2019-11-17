import turtle
import time
import random
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()
turtle.colormode(255)
RUNNING = True
SLEEP = 0.0099
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
MY_BALL = Ball(10,5,10,5,50,"red")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS =80
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS = []
for x in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	if (dx == 0):
		dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	if dy == 0:
		dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = random.randint (0,255), random.randint(0,255), random.randint(0,255)

	new_balls = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_balls)
def move_all_balls():
	for new_balls in BALLS:
		new_balls.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball_a, ball_b):
	ball_a_x = ball_a.xcor()
	ball_b_x = ball_b.xcor()
	ball_a_y = ball_a.ycor()
	ball_b_y = ball_b.ycor()
	ball_a_r = ball_a.r
	ball_b_r = ball_b.r
	if ball_a == ball_b:
		return False
	D = (((ball_b_x - ball_a_x)**2) + ((ball_b_y - ball_a_y)**2)**0.5)
	if D + 30 <= ball_a_r + ball_b_r:
		return True
	else:
		return False
def check_all_balls_collisions():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if (collide(ball_a,ball_b)) == True:
				ball_a_r = ball_a.r
				ball_b_r = ball_b.r
				new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				new_dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				if (new_dx == 0):
					new_dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				new_dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				if new_dy == 0:
					new_dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				new_radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				new_color = random.randint (0,255), random.randint(0,255), random.randint(0,255)

				if(ball_a_r  >ball_b_r):
					# BALLS.remove(ball_b)
					# ball_b.hideturtle()
					# ball_b.r = ball_b.r + 1
					# ball_b.shapesize(ball_b.r/10)
					ball_b.goto(new_x,new_y)
					ball_b.dx = new_dx
					ball_b.dy = new_dy
					ball_b.r = new_radius
					ball_b.color = new_color
					ball_a.r = ball_a.r + 1
					ball_a.shapesize(ball_a.r/10)



					# ball_b.setpos(random.randint(x,y), random.randint(x,y))
					# ball_b.showturtle()
					# ball_b.move()


				if (ball_b_r  > ball_a_r):
					# BALLS.remove(ball_a)
					ball_a.hideturtle()
					ball_a.goto(new_x,new_y)
					ball_a.dx = new_dx
					ball_a.dy = new_dy
					ball_a.r = new_radius
					ball_a.color = new_color
					ball_b.r = ball_a.r + 1
					ball_b.shapesize(ball_a.r/10)
					# ball_a.setpos(random.randint(x,y), random.randint(x,y))
					# ball_a.showturtle()
				if len(BALLS) == 0:
					return False
def check_myball_collision():
	for ball in BALLS:
		if (collide(ball, MY_BALL)) == True:
			new_x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			new_y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			new_dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			if (new_dx == 0):
				new_dx = random.randint (MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			new_dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			if new_dy == 0:
				new_dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
			new_radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			new_color = random.randint (0,255), random.randint(0,255), random.randint(0,255)

			ball_r = ball.r
			MY_BALL_r = MY_BALL.r
			if ball_r > MY_BALL_r:
				MY_BALL.hideturtle()
		 		return False
			if MY_BALL_r > ball_r:

				# MY_BALL.goto(new_x,new_y)
				# MY_BALL.dx = new_dx
				# MY_BALL.dy = new_dy
				# MY_BALL.r = new_radius
				# MY_BALL.color = new_color
				# ball.hideturtle()
				MY_BALL.r = MY_BALL.r + 1
				MY_BALL.shapesize(MY_BALL.r/10)
				# new_x = random.randint(x, y)
				# new_y = random.randint(x, y)
				# ball.setpos(random.randint(x, y),random.randint(x, y))
				# ball.showturtle()


def movearound():
	MY_BALL.ondrag(MY_BALL.setpos)


while RUNNING:
	check_all_balls_collisions()
	check_myball_collision()
	SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
	SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2
	move_all_balls()
	turtle.getscreen().update()
	turtle.time.sleep(SLEEP)
	movearound()
	if check_myball_collision() == False:
		RUNNING = False
	if len(BALLS) == 0:
		RUNNING = False


while RUNNING == False:

	turtle.write("game over", font = ("Arial" , 45 , "normal"))






turtle.exitonclick()

import turtle
from turtle import *
import random

class Ball (Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.speed(100)
		self.hideturtle()
		self.penup()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.showturtle()

	def move(self, screen_width, screen_height):
		self.screen_width = self.window_width()
		self.screen_height = self.window_height()
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		self.goto(new_x,new_y)
		right_side_ball = new_x + self.r
		top_side_ball = new_y + self.r
		left_side_ball = new_x - self.r
		bottom_side_ball = new_y - self.r

		if right_side_ball >= screen_width or left_side_ball <= -screen_width:
			self.dx = -self.dx
			self.clear()
		if (top_side_ball >= screen_height) or (bottom_side_ball<= -screen_height) :
			self.dy = -self.dy
			self.clear()





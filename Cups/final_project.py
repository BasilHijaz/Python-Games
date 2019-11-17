import pygame, time
from pygame.locals import *
from sys import exit


CUP_WIDTH = 120
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
cups_y = 70
cups_x = 80
middle_cup_y = cups_y
running = True
clicked = 0 


# drawing cups
def draw_cup(x, y):
	pygame.draw.ellipse(screen , (0,255,0), (x,y+146, CUP_WIDTH, 80))
	pygame.draw.rect(screen, (0,255,0), (x, y+40, CUP_WIDTH, 150))
	pygame.draw.ellipse(screen, (255,0,0), (x, y, CUP_WIDTH, 80))
# drawing a coin
def draw_coin(x,y):
	pygame.draw.circle(screen, (0,0,255), (x , y) , 25 , 0)


def draw_objects(cup_one_y, cup_two_y, cup_three_y, cup_one_x, cup_two_x, cup_three_x, show_Ball):
	pygame.draw.rect(screen , (204,102,0), (0,306,640,100))
	if show_Ball == True:
		draw_coin(ball_x, ball_y)

	draw_cup(cup_one_x + 340, cup_one_y)
	draw_cup(cup_two_x + 170, cup_two_y)
	draw_cup(cup_three_x, cup_three_y)

#making the cups fall down when click SPACE
def cups_cover_ball(cups_y):
	for i in range(50):
		cups_y += 2
		screen.fill((0,0,0))
		draw_objects(cups_y, cups_y, cups_y,cups_x,cups_x,cups_x, True)
		pygame.display.update()
		time.sleep(0.05)
	return cups_y
	return cups_x

#shuffling between middle_cup and last cup
def switch_A():
	for x in range(cups_x, cups_x + 180, +10):
		screen.fill((0,0,0))
		draw_objects(cups_y, cups_y,cups_y,cups_x,x,cups_x, False)
		pygame.display.update()
		time.sleep(0.05)
	crash_sound = pygame.mixer.Sound("crash.wav")
	pygame.mixer.Sound.play(crash_sound)
	pygame.mixer.music.load("cartoon172.wav")

#making the cup raise up
def cup_up():
	new_y = cups_y8
	for y in range(cups_y, cups_y - 180, -10):
		screen.fill((0,0,0))
		draw_objects(cups_y, y, cups_y, cups_x, cups_x, cups_x, False)
		pygame.display.update()
		time.sleep(0.05)
		new_y = y
	return new_y

#switching between the first cup and the middle one
def switch_B():
	for x in range(cups_x, cups_x + 180, +10):
		screen.fill((0,0,0))
		draw_objects(cups_y, cups_y, cups_y, cups_x, cups_x, x, False)
		pygame.display.update()
		time.sleep(0.05)
	crash_sound = pygame.mixer.Sound("crash.wav")
	pygame.mixer.Sound.play(crash_sound)
	pygame.mixer.music.load("cartoon172.wav")

#switching between the middle cup and the last cup
def switch_C():
 	for x in range(cups_x, cups_x - 180, -10):
		screen.fill((0,0,0))
		draw_objects(cups_y, cups_y, cups_y, cups_x, x, cups_x, False)
		pygame.display.update()
		time.sleep(0.05)
	crash_sound = pygame.mixer.Sound("crash.wav")
	pygame.mixer.Sound.play(crash_sound)
	pygame.mixer.music.load("cartoon172.wav")
# choosing cups
#winning & losing
def cup1_up(mouse_pos, start_over):
	global clicked
	mouse_x = mouse_pos[0]
	mouse_y = mouse_pos[1]
	clicked_cup = None
	if mouse_y >= cups_y and mouse_y <= cups_y + 200:
		if mouse_x >= 80 and mouse_x <= 80 + CUP_WIDTH:
			clicked_cup = "one"
		elif mouse_x >= 250 and mouse_x <= 250 + CUP_WIDTH:
			clicked_cup = "two"
		elif mouse_x >= 420 and mouse_x <= 420 + CUP_WIDTH:
			clicked_cup = "three"

	if clicked_cup == "one":
		clicked += 1
		for y in range(cups_y, cups_y - 125, -5):
			screen.fill((0,0,0))
			draw_objects(cups_y, cups_y, y, cups_x, cups_x, cups_x, True)
			pygame.display.update()
			time.sleep(0.05)
		if start_over == True:
			play_one_round(2)
		if clicked == 2:
			pygame.quit()
			exit()





	if clicked_cup == "two":
		for y in range(cups_y, cups_y - 125, -5):
			screen.fill((0,0,0))
			draw_objects(cups_y, y, cups_y, cups_x, cups_x, cups_x, True)
			pygame.display.update()
			time.sleep(0.05)
			img = pygame.image.load('game over.bmp')
			screen.fill((0,0,0))
			screen.blit(img,(0,0))
		if clicked == 2:
			pygame.quit()
			exit()



	if clicked_cup == "three":

		for y in range(cups_y, cups_y - 125, -5):
			screen.fill((0,0,0))
			draw_objects(y, cups_y, cups_y, cups_x, cups_x, cups_x, True)
			pygame.display.update()
			time.sleep(0.05)
		screen.fill((0,0,0))
		img = pygame.image.load('game over.bmp')
		screen.blit(img,(0,0))
	

		if clicked ==1:
			clicked=2



#rounds
def play_one_round(round_number):
	if round_number == 1:
		switch_A()
		switch_B()
		switch_A()
		switch_B()
		switch_C()
		switch_A()
		switch_B()
		switch_C()
		switch_B()
		switch_A()
		switch_C()

	if round_number == 2:
		switch_A()
		switch_B()
		switch_A()
		switch_C()
		switch_B()
		switch_A()
		switch_B()
		switch_C()
		switch_A()



before_round = True
ball_x = 310
ball_y = 356
running = True
rounds_done = 0 

while running:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

        if event.type == pygame.KEYDOWN:
        	if event.key == K_SPACE:	
        		cups_y = cups_cover_ball(cups_y)
        		play_one_round(1)
        		rounds_done += 1
        		before_round = False
        		ball_x = 140

        if event.type == pygame.MOUSEBUTTONUP:
        	pos = pygame.mouse.get_pos()
        	if rounds_done < 2:
        		cup1_up(pos, True)
        		rounds_done += 1

        	else:
        		cup1_up(pos, False)
        		screen.fill((0,0,0))
        	ball_x = 480

	draw_objects(cups_y, cups_y, cups_y, cups_x, cups_x, cups_x, True)

	if before_round:
		myfont = pygame.font.SysFont("monospace", 40)
		label = myfont.render("Press Space", 1, (255,0,255))
		screen.blit(label, (180, 50))

	if clicked == 2:
		screen.fill((0,0,0))
		k = pygame.image.load('congratulations.bmp')
		screen.blit(k,(100,170))


	pygame.display.update()
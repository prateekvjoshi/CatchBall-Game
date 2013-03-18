'''
A simple program to catch a bouncing ball. This utilizes Pygame. You should install it before you proceed.  

This is a very simple game. Just move the mouse and try to get the pointer over the ball.

'''

import sys, pygame, random
from pygame.locals import *

# Check if the fonts module loaded. 
if not pygame.font: print "Fonts disabled!"
pygame.init()
random.seed(pygame.time.get_ticks())

# Random numbers for some reason... hmm... what could r g b mean?
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

# Defining some initial values
size = width, height = 800, 600
xspeed = 5
yspeed = 5
incrementalSpeed = 0
speed = [xspeed, yspeed]
black = 0,0,0

# Setting up the screen the player sees. See how size comes from up there to down here? 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Catch the Ball!")

# Using convert_alpha() because we can use the PNG's transparency layer instead of defining it ourselves. This also helps speed things up as far as the game goes because the game doesn't have to keep converting the PNG file into a useable graphic format. .convert() does the same thing but does not include transparency.
ball = pygame.image.load('ball.png').convert_alpha()

# Loading the rect
ballrect = ball.get_rect()

# Setting the font color 
fontColor = r,g,b

# Setting the font
font = pygame.font.SysFont("Arial Black", 25)

# winText is a surface
winText = font.render('You caught the ball! [Click to Play Again]', 0, fontColor)

# Defining the window rect
winRect = [0,0,0,0]

# Defining the state of the ball: caught vs not caught
caught = 0

# How many ticks have passed since this was called?
tix = pygame.time.get_ticks()

# tixText = a surface
tixText = font.render(str(tix), 0, fontColor)

# Defining another rect for ticks
tixRect = [0,0,0,0]

# Number of times the user caught the ball
caughtAmt = 0
caughtText = font.render("Caught: " + str(caughtAmt), 0, fontColor)
caughtRect = [0,0,0,0]

# Main loop
while 1:
	# Update the ticks
	tix = pygame.time.get_ticks()
	tixText = font.render(str(tix), 0, fontColor)
	
	# Check some events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print "Quit event detected. Good bye!"
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			ding = event.pos
			
			# Did the mouse collide with the rect of the ball? Then the user caught the ball
			if ballrect.collidepoint(ding) and caught != 1:
				caught = 1
				caughtAmt = caughtAmt + 1
				caughtText = font.render("Caught: " + str(caughtAmt), 0, fontColor)
		
		# This only works when we caught the ball. If we click the mouse, then we get to go again.
		if event.type == pygame.MOUSEBUTTONUP:
			if caught == 1 and event.button == 1:
				caught = 0
				speed[0] = speed[0] + 1
				speed[1] = speed[1] + 1
	
	# Bouncing the ball: If the left-side of the ballrect is at or less than the 0 position of the left-hand side of the screen or it is greater than or equal to the right hand side of the screen, then we need to change the direction. Same thing for top and bottom.
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	
	# Fill the back of the screen with black
	screen.fill(black)
	
	# Draw us a ball
	screen.blit(ball, ballrect)
	
	# Draw the surface caughtText in the upper-right
	caughtRect = screen.blit(caughtText, (600, 0))
	
	# Draw the surface of the ticks counter in the upper-left
	tixRect = screen.blit(tixText, (0,0))
	
	# If we're currently in the "caught ball" state, then draw the winText and prevent the ball from moving.
	if caught == 1:
		winRect = screen.blit(winText, (50, 350))
		xspeed = xspeed + incrementalSpeed
		yspeed = yspeed + incrementalSpeed
		speed = [xspeed, yspeed]
	
	# Update everything
	updates = ballrect, tixRect, winRect, caughtRect
	pygame.display.update(updates)
	
	
	
	
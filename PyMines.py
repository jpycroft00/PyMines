import sys, pygame, field
from time import sleep

def terminate():
	sys.exit()

def checkInput():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			field.click(event)

def draw():
	while not field.gameOver:
		# print("drawing")
		checkInput()
		screen.fill(black)
		# print("drawing tiles (top level)")
		field.show(screen)
		# terminate()
		# sleep(1)

size = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
field = field.Field(30, 16, width, height, 99)
# field.generate()
pygame.init()
draw()
# field.show(screen)

    


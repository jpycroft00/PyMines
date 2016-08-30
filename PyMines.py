import sys, pygame, field
from time import sleep

def terminate():
	sys.exit()

def checkInput():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			field.click(event)
			draw()

def draw():
	# while not field.gameOver:
		# print("drawing")
		# checkInput()
		screen.fill(black)
		# print("drawing tiles (top level)")
		field.show(screen)
		score = font.render("Remaining: " + str(field.remainingMines), 15, white)
		screen.blit(score,(5,5,50,20))
		pygame.display.update()
		# terminate()
		# sleep(1)

size = width, height = 800, 600
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
field = field.Field(30, 16, width, height, 99)
font = pygame.font.SysFont('comicsans', 32, False, False)
score = font.render("Remaining: " + str(field.remainingMines), 15, white)
# field.generate()
pygame.init()
# field.show(screen)
draw()
while not field.gameOver:
	checkInput()

    


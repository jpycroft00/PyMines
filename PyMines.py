import sys, pygame, field
from time import sleep

def terminate():
    sys.exit()

def draw():
    while True:
        screen.fill(black)
        field.show()
        # terminate()

size = width, height = 640, 480
black = 0, 0, 0
white = 255, 255, 255
screen = pygame.display.set_mode(size)
field = field.Field(screen, 30, 16, width, height, 99)
pygame.init()
draw()


    


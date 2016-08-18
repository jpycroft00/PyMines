import sys, pygame
from time import sleep

class Tile:
	"""Tile object to store data regarding mine location in PyMines"""
	pygame.init()
	isMine = False
	adjacent = 0
	flagged = False
	opened = False
	pos = (x,y) = (0,0)
	width = 1
	black = (0,0,0)
	blue = (0,0,255)
	red = (255,0,0)
	font = pygame.font.SysFont('comicsans', 15, False, False)


	def __init__(self, x, y, width, isMine):
		if isMine:
			self.arm
		self.x = x
		self.y = y
		self.width = width

	#Arm the bomb
	def arm(self):
		self.isMine = True
		self.adjacent = 0
		
	def show(self, screen):
		pygame.draw.rect(screen, self.blue, (((self.pos[self.x]+1) * self.width), (self.pos[self.y] * self.width), self.width, self.width), 0)
		pygame.draw.rect(screen, self.black, (((self.pos[self.x]+1) * self.width), (self.pos[self.y] * self.width), self.width, self.width), 1)		
		
		if self.isMine:
			if self.opened:
				while False == pygame.font.get_init():
					sleep(10)
				label = font.render("X", self.width, red)
				
import sys, pygame

class Tile(object):
	"""Tile object to store data regarding mine location in PyMines"""
	isMine = false
	adjacent = 0
	flagged = false
	opened = false
	position = 0,0
	width = 1
	black = 0,0,0
	blue = 0,0,255
	font = pygame.font.SysFont("monospace", 15)

	def ___init___(self, x, y, width, mine)
		if mine
			self.arm
		self.x = x
		self.y = y
		self.width = width

	#Arm the bomb
	def arm(self)
		self.isMine = True
		self.adjacent = 0
		
	def show(self, screen)
		pygame.draw.rect(screen, self.blue, (self.pos[0] * self.width), (self.pos * self.width), self.width, 0)
		pygame.draw.rect(screen, self.black, (self.pos[0] * self.width), (self.pos * self.width), self.width, 1)		
		
		if self.isMine
			if self.opened
				pygame.draw.
import sys, pygame
from time import sleep

class Tile:
	"""Tile object to store data regarding mine location in PyMines"""
	pygame.init()
	isMine = False
	adjacent = 0
	flagged = False
	opened = False
	x,y = 0,0
	textGeometry = geometry = 0,0,0,0
	textOffset = 3
	w = 1
	black = (0,0,0)
	blue = (0,0,255)
	red = (255,0,0)
	white = (255,255,255)
	font = pygame.font.SysFont('comicsans', 32, False, False)
	label = font.render("", w, red)



	def __init__(self, x, y, w, isMine):
		if isMine:
			self.arm
		self.x = x
		self.y = y
		self.w = w
		self.geometry = (x,y,w,w)
		self.textGeometry = (x+self.textOffset,y,w,w)

	#Arm the bomb
	def arm(self):
		self.isMine = True
		self.adjacent = 0
		self.update()

	def open(self):
		if self.opened or self.flagged:
			print("Don't be silly")
		elif not self.opened:
			self.opened = True
		self.update()

	def flag(self):
		if self.opened:
			print("Don't be silly")
		elif self.flagged:
			self.flagged = False
		elif not self.flagged:
			self.flagged = True
		self.update()

	def update(self):
		if self.flagged:
			self.label = self.font.render("P", self.w, self.red)			
		elif self.isMine:
			self.label = self.font.render("X", self.w, self.red)
		elif self.adjacent != 0:
			self.label = self.font.render(str(self.adjacent), self.w, self.black)

		
	def show(self, screen):
		pygame.draw.rect(screen, self.blue, self.geometry, 0)
		pygame.draw.rect(screen, self.black, self.geometry, 1)

		if self.opened:
			pygame.draw.rect(screen, self.white, self.geometry, 0)
			pygame.draw.rect(screen, self.black, self.geometry, 1)
			screen.blit(self.label, self.textGeometry)
		if self.flagged:
			screen.blit(self.label, self.textGeometry)
				
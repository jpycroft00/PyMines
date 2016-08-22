import sys, pygame
from time import sleep

class Tile:
	"""Tile object to store data regarding mine location in PyMines"""
	pygame.init()
	isMine = False
	adjacent = 0
	flagged = False
	opened = True
	x,y = 0,0
	textGeometry = geometry = 0,0,0,0
	textOffset = 3
	w = 1
	black = (0,0,0)
	blue = (0,0,255)
	red = (255,0,0)
	font = pygame.font.SysFont('comicsans', 32, False, False)
	label = font.render("", w, red)



	def __init__(self, x, y, w, isMine):
		if isMine:
			self.arm
		self.x = x
		self.y = y
		self.w = w
		self.geometry = (self.x*self.w),(self.y*self.w),self.w,self.w
		self.textGeometry = (self.x*self.w)+self.textOffset,(self.y*self.w),self.w,self.w

	#Arm the bomb
	def arm(self):
		self.isMine = True
		self.adjacent = 0

	def update(self):
		if self.isMine:
			self.label = self.font.render("X", self.w, self.red)
		elif self.adjacent != 0:
			self.label = self.font.render(str(self.adjacent), self.w, self.black)

		
	def show(self, screen):
		pygame.draw.rect(screen, self.blue, self.geometry, 0)
		pygame.draw.rect(screen, self.black, self.geometry, 1)

		if self.opened:
			screen.blit(self.label, self.textGeometry)
				
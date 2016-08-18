import tile, pygame, random

class Field:
	tiles = list()
	mineCount = 0
	screen = 0
	def __init__(self, screen, geometryX , geometryY, displayX, displayY, mineCount): 	#Create an empty mine field as a 2D array of tiles
		self.screen = screen
		self.mineCount = mineCount
		x = 0
		tileWidth = int(displayX / (2 + geometryX)) 									#Calculate how wide each tile should be
		while x < geometryX:
			y=0
			self.tiles.append(list())
			while y < geometryY:
				self.tiles[x].append(tile.Tile(x,y,tileWidth,False))
				y += 1
			x += 1

	def generate(self): 																#Populate the mine field with mines and count adjacent mines
		####Populate the mine field with mines####
		i = 0
		while i < self.mineCount: 														#Set a random tile to be a mine, do this until all mines requested are generated
			randX = random.randint(0,len(tiles))
			randY = random.randint(0,len(tiles[0]))

			while tiles[randX][randY].isMine:											#Check if the randomly selected tile is already a mine, if so then find another random empty tile
				randX = random.randint(0,len(tiles))
				randY = random.randint(0,len(tiles[0]))

			tiles[randX][randY].arm()													#Finally actually set the mine on the tile
			i += 1

		####Populate the adjacent numbers####
		x = 0
		while x < len(self.tiles):
			y=0
			while y<len(self.tiles[0]):
				i=0
				if (x < (len(self.tiles)-1) and (y < (len(self.tiles[0])))) and (x > 0 and y > 0):#Do this if all surrounding tiles are still within the field
					if self.tiles[x-1][y-1].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x][y-1].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x+1][y-1].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x-1][y].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x+1][y].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x-1][y+1].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x][y+1].isMine:
						self.tiles[x][y].adjacent += 1
					if self.tiles[x+1][y+1].isMine:
						self.tiles[x][y].adjacent += 1
				elif x == 0:															#Do this if tiles are on the left edge
					if (y > 0) and (y < len(self.tiles[0])):
						if self.tiles[x+1][y].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x][y+1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x+1][y+1].isMine:
							self.tiles[x][y].adjacent += 1						
						if self.tiles[x][y-1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x+1][y-1].isMine:
							self.tiles[x][y].adjacent += 1
					elif y == 0:														#Do this if tile is in the top left corner
						if self.tiles[x+1][y].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x][y+1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x+1][y+1].isMine:
							self.tiles[x][y].adjacent += 1
					elif y == len(self.tiles[0]):											#Do this if tile is in the bottom left corner
						if self.tiles[x+1][y].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x][y-1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x+1][y-1].isMine:
							self.tiles[x][y].adjacent += 1

				elif x == len(self.tiles):													#Do this if tile is on the right edge
					if (y > 0) and (y < len(self.tiles[0])):
						if self.tiles[x-1][y].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x][y+1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x-1][y+1].isMine:
							self.tiles[x][y].adjacent += 1						
						if self.tiles[x][y-1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x-1][y-1].isMine:
							self.tiles[x][y].adjacent += 1
					elif y == 0:														#Do this if tile is in the top right corner
						if self.tiles[x-1][y].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x][y+1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x-1][y+1].isMine:
							self.tiles[x][y].adjacent += 1
					elif y == len(self.tiles[0]):											#Do this if tile is in the bottom right corner
						if self.tiles[x-1][y].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x][y-1].isMine:
							self.tiles[x][y].adjacent += 1
						if self.tiles[x-1][y-1].isMine:
							self.tiles[x][y].adjacent += 1

	def show(self):
		x=0
		while x < len(self.tiles):
			y=0
			while y < len(self.tiles[x]):
				self.tiles[x][y].show(self.screen)
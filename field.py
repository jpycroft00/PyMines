import tile, pygame, random

class Field:
	tiles = list()
	mineCount = 0
	tileWidth = 0
	gameOver = False
	generated = False
	xoff = 0
	yoff = 0
	def __init__(self, collumns , rows, displayX, displayY, mineCount): 	#Create an empty mine field as a 2D array of tiles
		self.mineCount = mineCount
		x = 0
		self.xoff = self.tileWidth = int(displayX / (2 + collumns)) 									#Calculate how wide each tile should be
		self.yoff = int(displayY / 3)-self.xoff
		while x < collumns:
			y=0
			self.tiles.append(list())
			while y < rows:
				xpos=(x*self.tileWidth)+self.xoff
				ypos=(y*self.tileWidth)+self.yoff
				self.tiles[x].append(tile.Tile(xpos,ypos,self.tileWidth,False))
				y += 1
			x += 1
		print((self.tiles[0][0].x,self.tiles[0][0].y))

	def generate(self, firstClick): 																#Populate the mine field with mines and count adjacent mines
		####Populate the mine field with mines####
		i = 0
		rangeX = range(firstClick[0]-1,firstClick[0]+1)
		print(rangeX)
		rangeY = range(firstClick[1]-1,firstClick[1]+1)
		print(rangeY)
		while i < self.mineCount: 														#Set a random tile to be a mine, do this until all mines requested are generated
			randX = random.randint(0,len(self.tiles)-1)
			randY = random.randint(0,len(self.tiles[0])-1)

			while self.tiles[randX][randY].isMine or (randX in rangeX and randY in rangeY):											#Check if the randomly selected tile is already a mine, if so then find another random empty tile
				randX = random.randint(0,len(self.tiles)-1)
				randY = random.randint(0,len(self.tiles[0])-1)

			self.tiles[randX][randY].arm()													#Finally actually set the mine on the tile
			# print((randX,randY))
			i += 1

		####Populate the adjacent numbers by checking surrounding tiles to see if they're mines####
		x = 0
		while x <len(self.tiles):
			y=0
			while y<len(self.tiles[0]):
				#### algorithm for calculating numbers using exceptions
				try:
					if self.tiles[x-1][y-1].isMine and x > 0 and y > 0:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:
					if self.tiles[x][y-1].isMine and y > 0:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:
					if self.tiles[x+1][y-1].isMine and y > 0:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:
					if self.tiles[x-1][y].isMine and x > 0:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:	
					if self.tiles[x+1][y].isMine:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:	
					if self.tiles[x-1][y+1].isMine and x > 0:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:	
					if self.tiles[x][y+1].isMine:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

				try:	
					if self.tiles[x+1][y+1].isMine:
						self.tiles[x][y].adjacent += 1
				except LookupError:
					pass
					# print("LookupError at " +str(x) + "," +str(y))

						
				### Algorithm for calculating numbers by detecting edge cases and avoiding them
				# if (x < (len(self.tiles)-1) and (y < (len(self.tiles[0])-1))) and (x > 0 and y > 0):#Do this if all surrounding tiles are still within the field
				# 	if self.tiles[x-1][y-1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x][y-1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x+1][y-1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x-1][y].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x+1][y].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x-1][y+1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x][y+1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x+1][y+1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# elif x == 0:															#Do this if tiles are on the left edge
				# 	if (y > 0) and (y < len(self.tiles[0])-1):
				# 		if self.tiles[x+1][y].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x+1][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1						
				# 		if self.tiles[x][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x+1][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 	elif y == 0:														#Do this if tile is in the top left corner
				# 		if self.tiles[x+1][y].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x+1][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 	elif y == len(self.tiles[0]):											#Do this if tile is in the bottom left corner
				# 		if self.tiles[x+1][y].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x+1][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1

				# elif x == len(self.tiles)-1:													#Do this if tile is on the right edge
				# 	if (y > 0) and (y < len(self.tiles[0])-1):
				# 		if self.tiles[x-1][y].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x-1][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1						
				# 		if self.tiles[x][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x-1][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 	elif y == 0:														#Do this if tile is in the top right corner
				# 		if self.tiles[x-1][y].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x-1][y+1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 	elif y == len(self.tiles[0])-1:											#Do this if tile is in the bottom right corner
				# 		if self.tiles[x-1][y].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# 		if self.tiles[x-1][y-1].isMine:
				# 			self.tiles[x][y].adjacent += 1
				# elif y == 0:
				# 	if self.tiles[x-1][y].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x-1][y+1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x][y+1].isMine:
				# 		self.tiles[x][y].adjacent += 1						
				# 	if self.tiles[x+1][y+1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x+1][y].isMine:
				# 		self.tiles[x][y].adjacent += 1

				# elif y == len(self.tiles[0])-1:
				# 	if self.tiles[x-1][y].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x-1][y-1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x][y-1].isMine:
				# 		self.tiles[x][y].adjacent += 1						
				# 	if self.tiles[x+1][y-1].isMine:
				# 		self.tiles[x][y].adjacent += 1
				# 	if self.tiles[x+1][y].isMine:
				# 		self.tiles[x][y].adjacent += 1
				self.tiles[x][y].update()
				y+=1
			x+=1
		print("jobs done")
		self.generated = True

	def show(self, screen):
		x=0
		# print(len(self.tiles))
		# print(len(self.tiles[x]))
		while x < len(self.tiles):
			# print(x)
			y=0
			while y < len(self.tiles[x]):
				# print(y)
				# print("drawing tiles (second level)")
				self.tiles[x][y].show(screen)
				if(self.tiles[x][y].isMine and self.tiles[x][y].opened):
					self.gameOver = True
				y+=1
			x+=1
		pygame.display.update()

	def click(self, event):
		if event.button == 1: #left click
			if not self.generated:
				indexX=int((event.pos[0]-self.xoff)/self.tileWidth)
				indexY=int((event.pos[1]-self.yoff)/self.tileWidth)
				self.generate((indexX,indexY))
			i=0
			while i < len(self.tiles):
				j=0
				while j < len(self.tiles[i]):
					x = self.tiles[i][j].x
					y = self.tiles[i][j].y
					w = self.tiles[i][j].w
					rangeX = range(x,x+w)
					rangeY = range(y,y+w)
					if event.pos[0] in rangeX and event.pos[1] in rangeY:
						self.tiles[i][j].open()
					j+=1
				i+=1


		elif event.button == 2: #middle click
			print("Not yet implemented")
			#placeholder for treelike opening of blank tiles

		elif event.button == 3: #right click
			# print("ye be a scurvy dawg")
			i=0
			while i < len(self.tiles):
				j=0
				while j < len(self.tiles[i]):
					x = self.tiles[i][j].x
					y = self.tiles[i][j].y
					w = self.tiles[i][j].w
					rangeX = range(x,x+w)
					rangeY = range(y,y+w)
					if event.pos[0] in rangeX and event.pos[1] in rangeY:
						self.tiles[i][j].flag()
					j+=1
				i+=1
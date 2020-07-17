import pygame
width = 1100
height = 650
fps = 60
striker_radius = height//15
peg_radius     = int(striker_radius//1.5)

class Striker():
	"""This is class for striker and peg"""
	def __init__(self,color,color_outline,radius,x, y):
		self.color         = color
		self.radius        = radius
		self.color_outline = color_outline
		self.x = x
		self.y = y
		self.position = (x, y)

	def get_position(self):
		return (self.position)

	def draw(self, win):
		pygame.draw.circle(win, self.color, self.position, self.radius,0)
		pygame.draw.circle(win,self.color_outline,self.position,self.radius,self.radius//10)

	def move(self):
		pos = pygame.mouse.get_pos()
		self.x = pos[0]
		self.y = pos[1]
		self.update()

	def update(self):
		self.position = (self.x, self.y)


class pegs(Striker):
	def __init__(self,color,color_outline,radius,x, y):
		super().__init__(color,color_outline,radius,x, y)
		self.vx, self.vy = 0, 0

	def draw(self, win):
		pygame.draw.circle(win,self.color,(self.x, self.y),self.radius,0)
		pygame.draw.circle(win,self.color_outline,(self.x, self.y),self.radius,self.radius//10)



	def move(self):
		if(self.y >= (height - peg_radius) or self.y <= peg_radius): #if gets at the lower wall (y of peg >=480) or upper wall( y of peg <= 20) 
			self.vy = (-1)*self.vy # just reverses the direction of the vy


		if(self.x >= (width - peg_radius) or self.x <= peg_radius): # if gets hit at right or the left wall respectively
			self.vx = (-1)*self.vx # just reverses the direction of vx

		self.x += self.vx
		self.y += self.vy
		self.update()

import pygame
import socket
from player import Player
import pickle
import math
import time



width = 500
height = 500
win = pygame.display.set_mode((width, height)) #window intialized
pygame.display.set_caption("Client") #Caption set


class Network:
	def __init__(self): #constructor
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = socket.gethostname()
		self.port = 5555
		self.addr = (self.server, self.port)
		self.LIST= self.connect() #self.LIST = [player1, peg]
		self.p = self.LIST[0]
		self.peg = self.LIST[1]

	def getP(self):
		return self.p

	def getPeg(self):
		return self.peg

	def connect(self): 
		try:
			self.client.connect(self.addr) #connects with the server
			return pickle.loads(self.client.recv(2048)) #receives a list of player1 object and peg from the server 
		except:
			pass

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data)) #sends the [player1, peg] to the server
			return pickle.loads(self.client.recv(2048)) # receives [player2, peg]
		except socket.error as e:
			print(e)


def round_off(x): #this function rounds of  decimal... if so if 0<x<1 the return 1 else if {x}>=0.5 return [x+1]  else return [x]
	if 0.0<x<1.0:
		return 1

	y = x - int(x)

	if(y>=(0.5)):
		return int(x+1)

	else:
		return int(x)

def rel_vec(peg, player):
	return round_off((peg[0] - player[0])), round_off((peg[1] - player[1]))


def redrawWindow(win,player, player2, peg):
	win.fill((255,255,255))
	player.draw(win)
	player2.draw(win)
	peg.draw(win)
	pygame.display.update()



def dist(x, y):
	return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)])) #distance function

def main():
	run = True
	n = Network() #creates an instance of the network connection with server
	p = n.getP() # p is the object of (player 1)
	peg = n.getPeg() # object of the peg
	clock = pygame.time.Clock()

	while run:
		clock.tick(60)
		player2_obj, peg_obj = n.send([p, peg]) #sends the list of object of the player1 to the server and gets back the object of player2
		p2 = player2_obj #player 2 object
		peg = peg_obj #peg object
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()


		rx, ry= rel_vec(peg.get_point(), p.get_point()) # [rx , ry] is the relative vector of the peg wrt the striker

		print(rx, ry)

		p.move()  #this handles the movement of player , so when you move the mouse the move() method gets the mouse position and postions the player on the mouse pointer 
		peg.move() #this handles the movement of the peg , this includes the bouncing of the wall

		redrawWindow(win, p, p2, peg) #after each change in the respective positions of player and peg the screen is updated....

main()

import pygame
import socket
from player import Player
from Queue import queue
import pickle
import math
import time

def get_time():
	return int(round(time.time() * 1000))




class Network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = socket.gethostname()
		self.port = 5555
		self.addr = (self.server, self.port)
		self.LIST= self.connect()
		self.p = self.LIST[0]
		self.peg = self.LIST[1]

	def getP(self):
		return self.p

	def getPeg(self):
		return self.peg

	def connect(self):
		try:
			self.client.connect(self.addr)
			return pickle.loads(self.client.recv(2048))
		except:
			pass

	def send(self, data):
		try:
			self.client.send(pickle.dumps(data))
			return pickle.loads(self.client.recv(2048))
		except socket.error as e:
			print(e)

def deter(x):
	neg = (x<0)
	

	val = abs(x)
	ret = 0
	if(val<1):
		ret = 1

	y = val - int(val)

	if(y>=(0.5)):
		ret = int(val+1)

	else:
		ret = int(val)

	if(neg):
		return -1*ret

	else:
		return ret


def rel_vec(peg, player, t):
	return deter((peg[0] - player[0])), deter((peg[1] - player[1]))

def dotproduct(v1, v2):
	return sum((a*b) for a, b in zip(v1, v2))

def length(v):
	return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
	return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))    

def corner(l):
	v1 = [(l[0][0] - l[1][0]), (l[0][1] - l[1][1])]
	v2 = [(l[1][0] - l[2][0]), (l[1][1] - l[2][1])]
	return math.degrees(angle(v1, v2))


# def deter():
# 	if(self.y >= 450 and self.y <= 41):
# 		vy=(-1)*vy

# 	if(self.x >= 450 and self.x <= 41):
# 		vx=(-1)*vx

# 	self.x += vx
# 	self.y += vy
# 	self.update()



# width = 1900
# height = 900
width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")





def redrawWindow(win,player, player2, peg, rx, ry):
	win.fill((255,255,255))
	player.draw(win)
	player2.draw(win)
	if(peg != 0):
		peg.draw(win)
	pygame.draw.line(win, (0, 0, 0), player.get_point(), (100+rx, 110+ry), 4)
	pygame.display.update()

def hit():
	return True


def dist(x, y):
	return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

def main():
	run = True
	n = Network()
	p = n.getP()
	peg = n.getPeg()
	clock = pygame.time.Clock()
	points = queue(2)
	time_stamps = queue(2)
	vel_mag = 0
	ctr =0
	point = 0
	rx = 0
	ry = 0
	while run:
		clock.tick(60)
		recevd = n.send([p, peg])
		p2 = recevd[0]
		peg = recevd[1]
		# print(p2)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()



		ctr+=1


		# if(len(points.q) <2):
		# 	continue
		try:
			if(ctr%10 == 0):

				rx, ry= rel_vec(peg.get_point(), p.get_point(), time_stamps)

				ctr = 0

			# direction = (((points.q)[1][0] - (points.q)[0][0]), ((points.q)[1][1] - (points.q)[0][1]))
			# print(direction)
			# print(peg.get_point())
			print(rx, ry)
			


			
			if(hit()):
				pass

		except:
			pass

		p.move()

		# deter_vel = deter()

		if(peg != 0):
			# if(tup[0])
			peg.move()
			print(peg.vx, peg.vy)

		redrawWindow(win, p, p2, peg, rx, ry)

main()

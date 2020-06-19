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
		self.p = self.connect()

	def getP(self):
		return self.p

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






width = 1900
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win,player, player2):
	win.fill((255,255,255))
	player.draw(win)
	player2.draw(win)
	pygame.display.update()

def hit():
	return True


def dist(x, y):
	return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

def main():
	run = True
	n = Network()
	p = n.getP()
	clock = pygame.time.Clock()
	points = queue(2)
	time_stamps = queue(2)
	vel_mag = 0
	ctr =0
	point = 0
	while run:
		clock.tick(60)
		p2 = n.send(p)
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
				points.push(p.get_point())
				time_stamps.push()
				vel = dist(points[1], points[0])//abs(time_stamps[1] - time_stamps[0])
				vel = int(vel)
				ctr = 0

			direction = (((points.q)[1][0] - (points.q)[0][0]), ((points.q)[1][1] - (points.q)[0][1]))
			print(direction)
			if(hit()):
				pass

		except:
			pass

		p.move()

		redrawWindow(win, p, p2)

main()
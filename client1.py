import pygame,time,math
import sys,os #using this module to debug
from network import *
from participant import *

pygame.init()

size           = width, height = 1100,650
striker_radius = height//15
peg_radius     = int(striker_radius//1.5)

black          = (0,0,0) 
white          = (255,255,255)
blue           = (0,0,255)
red            = (255,0,0)
green          = (0,255,0)
light_green    = (0,200,0)
exit_game      = False
mouse_pos      = (width- striker_radius,height//2)#initial position of striker
game_display   = pygame.display.set_mode(size)
pygame.display.set_caption("Air Hockey")
fps = 60
		



def make_ground():

	game_display.fill((0, 0, 0))
	pygame.draw.line  (game_display,white, (width//2,0),(width//2,height)  ,3)
	pygame.draw.line  (game_display,white, (width,200), (width,400)        ,20)
	pygame.draw.line  (game_display,white, (0,200), (0,400)                ,20)
	pygame.draw.rect  (game_display,red  , (0,0,width,height)              ,4)
	pygame.draw.circle(game_display,white, (width//2,height//2),height//6  ,3)

def redrawWindow(win,player1, player2 ,peg):
	player1.draw(win)
	player2.draw(win)
	peg.draw(win)
	pygame.display.update()

def game_loop(exit_game,mouse_pos):
	n = Network()
	player1 = n.getP()
	peg = n.getPeg()
	peg_x = width//2
	peg_y = height//2
	clock = pygame.time.Clock()
	while not exit_game:
		clock.tick(60)
		player2, peg = n.send([player1, peg])
		make_ground()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game = True
				quit()

		player1.move()
		peg.move()
		# hit = if_hit(player1,peg)
		# if hit is not False:
		# 	print(hit)
		# 	peg.vx, peg.vy = hit

		# hit = if_hit(player2, peg)
		# if hit is not False:
		# 	print(hit, "p2")
		# 	peg.vx, peg.vy = hit

		pygame.draw.line(game_display,green,peg.get_position(),player1.get_position())
		redrawWindow(game_display, player1, player2, peg)


game_loop(exit_game,mouse_pos)

import pygame
class Peg():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.position = (x,y)
        self.radius = radius
        self.vx, self.vy = 1, 1

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius )

    def get_point(self):
        return self.position

    def move(self):
        # pos = pygame.mouse.get_pos()
        if(self.y >= 480 or self.y <= 20): #if gets at the lower wall (y of peg >=480) or upper wall( y of peg <= 20) 
            self.vy = (-1)*self.vy # just reverses the direction of the vy


        if(self.x >= 480 or self.x <= 20): # if gets hit at right or the left wall respectively
            self.vx = (-1)*self.vx # just reverses the direction of vx

        self.x += self.vx
        self.y += self.vy
        self.update()

    def update(self):
        self.position = (self.x, self.y)

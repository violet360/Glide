import pygame
class Peg():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = (x,y)
        # self.vel = 3
        self.radius = radius
        self.vx, self.vy = 1, 1

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius )

    def get_point(self):
        return (self.x, self.y)

    def move(self):
        # pos = pygame.mouse.get_pos()
        if(self.y >= 480 or self.y <= 20):
            self.vy = (-1)*self.vy


        if(self.x >= 480 or self.x <= 20):
            self.vx = (-1)*self.vx

        self.x += self.vx
        self.y += self.vy
        self.update()

    def update(self):
        self.rect = (self.x, self.y)

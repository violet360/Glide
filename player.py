import pygame
class Player():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = (x,y)
        self.vel = 3
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius )

    def get_point(self):
        return (self.x, self.y)

    def move(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]

        self.update()

    def update(self):
        self.rect = (self.x, self.y)

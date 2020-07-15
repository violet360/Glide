import pygame
class Player():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.color = color
        self.position = (x,y)
        self.radius = radius

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius )

    def get_point(self):
        return self.position

    def move(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]

        self.update()

    def update(self):
        self.position = (self.x, self.y)


#trust me u don't need comments here it's plain english, if you do perhaps some mandarin might add value 

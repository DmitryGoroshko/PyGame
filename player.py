from pygame import *

SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xspeed = 0
        self.yspeed = 0
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right):
        if left:
            self.xspeed = -SPEED
        if right:
            self.xspeed = SPEED
        if not(left or right):
            self.xspeed = 0

        self.rect.x += self.xspeed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

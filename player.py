from pygame import *

#phisycal const
SPEED = 7
JUMP = 10
GRAVITY = 0.35

#size and color
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xspeed = 0
        self.yspeed = 0
        self.onGround = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up):
        if left:
            self.xspeed = -SPEED
        if right:
            self.xspeed = SPEED
        if not(left or right):
            self.xspeed = 0
        if up:
            if self.onGround:
                self.yspeed = -JUMP

        if not  self.onGround:
            self.yspeed += GRAVITY
        self.onGround = False

        self.rect.y += self.yspeed
        self.rect.x += self.xspeed

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

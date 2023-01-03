from pygame import *
import pyganim

# phisycal const
SPEED = 4
JUMP = 12
GRAVITY = 0.35

# size and color
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

# animation
ANIMATION_DELAY = 200  # frame rate
ANIMATION_RIGHT = [('mario/r2.png'),
                   ('mario/r3.png'),
                   ('mario/r4.png'),
                   ('mario/r5.png')
                   ]
ANIMATION_LEFT = [('mario/l2.png'),
                  ('mario/l3.png'),
                  ('mario/l4.png'),
                  ('mario/l5.png')
                  ]
ANIMATION_JUMP_LEFT = [('mario/jl.png', 100)]
ANIMATION_JUMP_RIGHT = [('mario/jr.png', 100)]
ANIMATION_JUMP = [('mario/j.png', 100)]
ANIMATION_STAY = [('mario/0.png', 100)]

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xspeed = 0
        self.yspeed = 0
        self.onGround = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

        self.image.set_colorkey(Color(COLOR)) #прозрачный фон

        #move right
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        #move left
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()



    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yspeed = -JUMP
            self.image.fill(Color(COLOR))
            self.boltAnimJump.blit(self.image, (0, 0))

        if left:
            self.xspeed = -SPEED
            self.image.fill(Color(COLOR))
            if up:  # для прыжка влево есть отдельная анимация
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xspeed = SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xspeed = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.boltAnimStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yspeed += GRAVITY
        self.onGround = False

        self.rect.y += self.yspeed
        self.collide(0, self.yspeed, platforms)

        self.rect.x += self.xspeed
        self.collide(self.xspeed, 0, platforms)

    def collide(self, xspeed, yspeed, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xspeed > 0:
                    self.rect.right = p.rect.left
                if xspeed < 0:
                    self.rect.left = p.rect.right
                if yspeed > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yspeed = 0
                if yspeed < 0:
                    self.rect.top = p.rect.bottom
                    self.yspeed = 0

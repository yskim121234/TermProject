import pygame as pg
from Character.Animation import Animation
# Character State
IDLE = 0
WALK = 1
RUN  = 2

class Character(pg.sprite.Sprite):

    def __init__(self, position):
        super(Character, self).__init__()
        # Character Size
        self.size = (200, 200)
        
        # Player Direction
        self.direction = 0

        # Idle Animation
        self.animations = []
        self.animations.append(Animation('./Asset/Character/Girl/Idle', self.size))
        self.animations.append(Animation('./Asset/Character/Girl/Walk', self.size))
        

        # init state
        self.idle()

        # init options
        self.rect = pg.Rect(position, self.size)

        self.index = 0
        self.image = self.animations[IDLE].image

        self.speed = 5

        self.is_jumping = False
        self.movey = 20

        self.clear = False

        self.keys = pg.key.get_pressed()

    def control(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
                self.jump()

        if keys[pg.K_a] - keys[pg.K_d] != 0:
            self.walk(keys[pg.K_d] - keys[pg.K_a])

        else:
            self.idle()

    def update(self):
        # play animation   
        self.control()

         # player move
        if self.state == WALK:
            self.rect.x += self.direction * self.speed
        
        # player Jump    
        if self.is_jumping:
            self.rect.y -= self.movey
            self.movey -= 1
            if self.movey < -20:
                self.is_jumping = False
                self.movey = 20
            if self.direction < 0:
                self.image = pg.transform.flip(
                            pg.transform.scale(
                            pg.image.load('./Asset/Character/Girl/Jump/Jump (17).png'), self.size), True, False)
                return
            else:
                self.image = pg.transform.scale(pg.image.load('./Asset/Character/Girl/Jump/Jump (17).png'), self.size)
                return
            
        if self.direction < 0:
            self.image = pg.transform.flip(self.animations[self.state].update(), True, False)
            return
        else:
            self.image = self.animations[self.state].update()

    def idle(self):
        self.state = IDLE

    def walk(self, direction):

        if direction == 0:
            return
        
        self.state = WALK
        
        self.direction = direction
        
    def jump(self):
        # jumping
        self.is_jumping = True
        
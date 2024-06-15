import pygame as pg
from Character.Animation import Animation
# Character State
UP = 0
RIGHTUP = 1
RIGHT = 2
RIGHTDOWN = 3
DOWN = 4
LEFTDOWN = 5
LEFT = 6
LEFTUP = 7


class Car(pg.sprite.Sprite):

    def __init__(self, position):
        super(Car, self).__init__()
        # Character Size
        self.size = (300, 300)
        
        # Player Direction
        self.direction = UP

        # images
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarU.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarRU.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarR.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarRD.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarD.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarLD.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarL.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarLU.png'), self.size))

        # init options
        self.rect = pg.Rect(position, self.size)

        self.image = self.images[self.direction]

        self.speed = 0
        self.maxspeed = 20

        self.keys = pg.key.get_pressed()

    def control(self):
        keys = pg.key.get_pressed()

        direction = (keys[pg.K_d] - keys[pg.K_a], keys[pg.K_w] - keys[pg.K_s])

        if direction == (0, 1):
            self.direction = UP
        elif direction == (1, 1):
            self.direction = RIGHTUP
        elif direction == (1, 0):
            self.direction = RIGHT
        elif direction == (1, -1):
            self.direction = RIGHTDOWN
        elif direction == (0, -1):
            self.direction = DOWN
        elif direction == (-1, -1):
            self.direction = LEFTDOWN
        elif direction == (-1, 0):
            self.direction = LEFT
        elif direction == (-1, 1):
            self.direction = LEFTUP
        
        if keys[pg.K_SPACE] - keys[pg.K_LSHIFT] == 0:
            if self.speed < 0:
                self.speed += 0.02
            elif self.speed > 0:
                self.speed -= 0.02
            
            if self.speed < 0.1 and self.speed > -0.1:
                self.speed = 0
        else:
            if self.speed <= self.maxspeed and self.speed >= -self.maxspeed:
                self.speed += (keys[pg.K_SPACE] - keys[pg.K_LSHIFT]) * 0.1
            if self.speed >= self.maxspeed:
                self.speed = self.maxspeed
            if self.speed <= -self.maxspeed:
                self.speed = -self.maxspeed
        
        
    def update(self):
        # play animation   
        self.control()

        self.image = self.images[self.direction]

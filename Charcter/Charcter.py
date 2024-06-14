import pygame as pg
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
        self.idle_images = []
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (1).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (2).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (3).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (4).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (5).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (6).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (7).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (8).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (9).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (10).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (11).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (12).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (13).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (14).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (15).png'))
        self.idle_images.append(pg.image.load('./Asset/Character/Girl/Idle/Idle (16).png'))
        for i in range(len(self.idle_images)):
            self.idle_images[i] = pg.transform.scale(self.idle_images[i], self.size)

        # Walk Animation
        self.walk_images = []
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (1).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (2).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (3).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (4).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (5).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (6).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (7).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (8).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (9).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (10).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (11).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (12).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (13).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (14).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (15).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (16).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (17).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (18).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (19).png'))
        self.walk_images.append(pg.image.load('./Asset/Character/Girl/Walk/Walk (20).png'))
        for i in range(len(self.walk_images)):
            self.walk_images[i] = pg.transform.scale(self.walk_images[i], self.size)

        # init state
        self.idle()

        # init options
        self.rect = pg.Rect(position, self.size)

        self.index = 0
        self.image = self.images[self.index]

        self.speed = 5

        self.is_jumping = False
        self.movey = 20

        self.clear = False

        self.keys = pg.key.get_pressed()

    def control(self):
        keys = self.keys
        if keys[pg.K_SPACE]:
                self.jump()

        if keys[pg.K_a] - keys[pg.K_d] != 0:
            self.walk(keys[pg.K_d] - keys[pg.K_a])

        elif self.state != IDLE:
            self.idle()
    def update(self):
        
        self.keys = pg.key.get_pressed()
        self.control()
        # play animation    
        self.index += 1

        # loop animation
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

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
            
            # player direction in jump state
            if self.direction < 0:
                self.image = pg.transform.flip(pg.transform.scale(pg.image.load('./Asset/Character/Girl/Jump/Jump (17).png'), self.size), True, False)
            else:
                self.image = pg.transform.scale(pg.image.load('./Asset/Character/Girl/Jump/Jump (17).png'), self.size)

    def idle(self):
        self.state = IDLE

        # set animation - idle    
        if self.direction < 0:
           self.images = [pg.transform.flip(image, True, False) for image in self.idle_images]
        else:
            self.images = self.idle_images
   

    def walk(self, direction):

        if direction == 0:
            return
        
        self.state = WALK
        
        self.direction = direction

        if self.is_jumping:
            return
        
        # set animation - walk
        if direction < 0:
           self.images = [pg.transform.flip(image, True, False) for image in self.walk_images]
        else:
            self.images = self.walk_images
        
    def jump(self):
        # jumping
        self.is_jumping = True
        
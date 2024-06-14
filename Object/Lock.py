import pygame as pg

class Lock(pg.sprite.Sprite):

    def __init__(self, Object):
        super(Lock, self).__init__()

        Object.locked = True
        self.object = Object
        self.rect = Object.rect
        size = (self.rect.w, self.rect.h)
        self.image = pg.image.load('./Asset/Object/Lock.png')
        self.image.convert_alpha()
        self.image.set_colorkey((0,255,0))
        self.image = pg.transform.scale(self.image, size)

    def update(self):
        if self.object.locked:
            return
        self.kill()
        
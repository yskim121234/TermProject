import pygame as pg

class Platform(pg.sprite.Sprite):
    
    def __init__(self, x, y, w, h):
        super(Platform, self).__init__()

        size = (w, h)
        self.image = pg.image.load('./Asset/Object/image.png')
        self.image.convert_alpha()
        self.image.set_colorkey((0,255,0))
        self.rect = pg.Rect(x, y, w, h)
        self.image = pg.transform.scale(self.image, size)


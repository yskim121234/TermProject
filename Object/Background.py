import pygame as pg

class Sky(pg.sprite.Sprite):
    
    def __init__(self, x, y, w, h):
        super(Sky, self).__init__()

        size = (w, h)
        self.image = pg.image.load('./Asset/Object/Sky.jpg')
        self.image.convert_alpha()
        self.image.set_colorkey((0,255,0))
        self.rect = pg.Rect(x, y, w, h)
        self.image = pg.transform.scale(self.image, size)
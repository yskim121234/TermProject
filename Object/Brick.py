import pygame as pg
import numpy

class Brick():
    def __init__(self, x, y, w, h):
        # 부모 생성자 호출
        super(Brick, self).__init__()
        
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Brick/Blue.png'),(w, h))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

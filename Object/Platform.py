import pygame as pg

class Platform(pg.sprite.Sprite):
    
    def __init__(self, x, y, w, h):
        super(Platform, self).__init__()

        # 사이즈
        size = (w, h)
        # 이미지 불러오고 사이즈 조절하여 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/image.png'), size)
        # Rect 생성
        self.rect = pg.Rect(x, y, w, h)


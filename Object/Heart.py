import pygame as pg

class Heart(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Heart, self).__init__()
        # 하트 이미지의 사이즈를 수정하여 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Heart.png'), (30, 30))
        # 이미지의 Rect 저장
        self.rect = self.image.get_rect()
        # Rect의 위치 수정
        self.rect.topleft = (x, y)
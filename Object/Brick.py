import pygame as pg

class Brick(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        # 부모 생성자 호출
        super(Brick, self).__init__()
        
        # 벽돌 이미지를 불러오고 사이즈를 수정하여 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Brick/Blue.png'),(w, h))
        # 이미지의 마스크 저장
        self.mask = pg.mask.from_surface(self.image)
        # 이미지의 Rect 저장
        self.rect = self.image.get_rect()
        # Rect의 위치 수정
        self.rect.topleft = (x, y)

import pygame as pg

class Sky(pg.sprite.Sprite):
    
    def __init__(self, x, y, w, h):
        super(Sky, self).__init__()
        
        # 사이즈
        size = (w, h)

        # 하늘 이미지 불러오기
        self.image = pg.image.load('./Asset/Object/Sky.jpg')
        # 이미지 크기 조절
        self.image = pg.transform.scale(self.image, size)
        # Rect 생성
        self.rect = pg.Rect(x, y, w, h)
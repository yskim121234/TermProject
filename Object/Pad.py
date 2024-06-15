import pygame as pg

class Pad(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        # 부모 생성자 호출
        super(Pad, self).__init__()

        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Pad/Blue.png').convert_alpha(), (w, h))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # 색
        self.color = 'white'
        # 최대 X 범위
        self.Max_Range_X = None

    # 키보드 이동
    def update(self):
        keys = pg.key.get_pressed()
        # 키에 따라 이동
        # 왼쪽(-X) 이동시 : (0 - 1)*10 = -1*10 = -10
        # 오른쪽(X) 이동시: (1 - 0)*10 = 1*10 = 10
        self.rect.x += (keys[pg.K_d] - keys[pg.K_a]) * 10
        
        # 최대 X 범위가 지정되었을 경우
        if self.Max_Range_X != None:
            # 왼쪽 벽에 충돌한 경우
            if self.rect.x < 0:
                self.rect.x = 0
            # 오른쪽 벽에 충돌한 경우
            if self.rect.x > self.Max_Range_X-self.rect.w:
                self.rect.x = self.Max_Range_X-self.rect.w
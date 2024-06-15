import pygame as pg

class Pad(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        # 부모 생성자 호출
        super(Pad, self).__init__()

        # 패드 이미지를 불러오고 투명한 부분을 투명하게 만들고 사이즈를 조절하여 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Pad/Blue.png').convert_alpha(), (w, h))
        # 이미지의 마스크 저장
        self.mask = pg.mask.from_surface(self.image)
        # 이미지의 Rect 저장
        self.rect = self.image.get_rect()
        # Rect의 위치 변경
        self.rect.topleft = (x, y)
        # 최대 X 범위 설정
        self.Max_Range_X = pg.display.get_window_size()[0]

    # 키보드 이동
    def update(self):
        keys = pg.key.get_pressed()
        # 키에 따라 이동
        self.rect.x += (keys[pg.K_d] - keys[pg.K_a]) * 10
        
        # 왼쪽 벽에 충돌한 경우
        if self.rect.x < 0:
            self.rect.x = 0
        # 오른쪽 벽에 충돌한 경우
        if self.rect.x > self.Max_Range_X-self.rect.w:
            self.rect.x = self.Max_Range_X-self.rect.w
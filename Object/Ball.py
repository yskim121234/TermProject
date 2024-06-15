import pygame as pg
import numpy

class Ball(pg.sprite.Sprite):
    def __init__(self, size, x=0, y=0):
        #부모 생성자 호출
        super(Ball, self).__init__()

        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Ball/Blue.png').convert_alpha(), (size, size))
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        # 색
        self.color = 'white'
        
        # 기본 속도
        self.Base_Speed = 5

        # 축 속도
        self.Speed_X = 0
        self.Speed_Y = 0

        #최대 범위 0~
        self.Max_Range_X, self.Max_Range_Y = pg.display.get_window_size()
        
        #발사 준비
        self.Is_Ready = True

    # 발사
    def Shot(self):
        keys = pg.key.get_pressed()

        # 스페이스바가 눌렸을 경우
        if keys[pg.K_SPACE]:
            self.Speed_Y = -self.Base_Speed * numpy.cos(45)

            # ranint의 범위는 0~1 => False or True
            if numpy.random.randint(0,2):
                self.Speed_X = self.Base_Speed * numpy.sin(45)
            else:
                self.Speed_X = -self.Base_Speed * numpy.sin(45)
            #발사 준비 상태 해제
            self.Is_Ready = False

    def update(self):
        if self.Is_Ready:
            self.Shot()
        # 각 축에 속도를 더함
        self.rect.x += self.Speed_X 
        self.rect.y += self.Speed_Y

        # 왼쪽 벽과 충돌 시
        if self.rect.x <= 0:
            self.Speed_X = -self.Speed_X
            self.rect.x = 0
        # 오른쪽 벽과 충돌 시
        if self.rect.x >= self.Max_Range_X-self.rect.w:
            self.Speed_X = -self.Speed_X
            self.rect.x = self.Max_Range_X-self.rect.w

        #천장과 충돌 시
        if self.rect.y <=0:
            self.Speed_Y = -self.Speed_Y
            self.rect.centery = 1
        #바닥과 충돌 시
        if self.rect.y + self.rect.h >= self.Max_Range_Y:
            #죽음
            self.kill()
        
    
    # 위치 및 속도 초기화
    def Reset(self, pad):
        self.Speed_X = 0
        self.Speed_Y = 0
        self.rect.x = pad.rect.centerx-self.rect.w/2
        self.rect.y = pad.rect.y-self.rect.h
        
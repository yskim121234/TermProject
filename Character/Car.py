import pygame as pg
import numpy as np
from numba import *

# 방향 매크로
UP = 0
RIGHTUP = 1
RIGHT = 2
RIGHTDOWN = 3
DOWN = 4
LEFTDOWN = 5
LEFT = 6
LEFTUP = 7


class Car(pg.sprite.Sprite):

    def __init__(self, position):
        super(Car, self).__init__()
        # 사이즈
        self.size = (300, 300)
        
        # 방향 초기화
        self.direction = UP

        # 방향별 이미지
        self.images = []
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarU.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarRU.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarR.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarRD.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarD.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarLD.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarL.png'), self.size))
        self.images.append(pg.transform.scale(pg.image.load('./Asset/Object/Car/CarLU.png'), self.size))

        # Rect 객체 생성
        self.rect = pg.Rect(position, self.size)

        # 현재 이미지
        self.image = self.images[self.direction]

        # 속도
        self.speed = 0
        # 최대 속도
        self.maxspeed = 20
        
        pg.mixer.Sound('./Asset/Object/Car/Start_up.wav').play()

    def control(self):
        # 입력 중인 키보드 키 리스트
        keys = pg.key.get_pressed()

        # 방향을 (x, y)로 저장
        direction = (keys[pg.K_d] - keys[pg.K_a], keys[pg.K_w] - keys[pg.K_s])

        # 방향 변수 변경
        if direction == (0, 1):
            self.direction = UP
        elif direction == (1, 1):
            self.direction = RIGHTUP
        elif direction == (1, 0):
            self.direction = RIGHT
        elif direction == (1, -1):
            self.direction = RIGHTDOWN
        elif direction == (0, -1):
            self.direction = DOWN
        elif direction == (-1, -1):
            self.direction = LEFTDOWN
        elif direction == (-1, 0):
            self.direction = LEFT
        elif direction == (-1, 1):
            self.direction = LEFTUP
        
    def move(self):
        drive = pg.mixer.Sound('./Asset/Object/Car/Drive.wav')
        drive.set_volume(0.06 + (0.09/20 * np.abs(self.speed)))
        if pg.mixer.get_busy() == False:
            drive.play(0, 100)

        keys = pg.key.get_pressed()
         # 만약 전진이나 후진을 하지 않고 있다면
        if keys[pg.K_SPACE] - keys[pg.K_LSHIFT] == 0:
            # 속도를 서서히 0에 수렴하게 함.
            if self.speed < 0:
                self.speed += 0.02
            elif self.speed > 0:
                self.speed -= 0.02
            
            # Float의 오차를 생각해 값이 일정 범위 내에 들어오면 0으로 설정
            if self.speed < 0.1 and self.speed > -0.1:
                self.speed = 0
        else:
            # 현재 속도가 최대 속도 이하라면
            if self.speed <= self.maxspeed and self.speed >= -self.maxspeed:
                # 키 입력에 따라 전진 혹은 후진
                self.speed += (keys[pg.K_SPACE] - keys[pg.K_LSHIFT]) * 0.1
            
            # 최대 속도의 범위를 넘어설 경우를 대비하여 제한
            if self.speed >= self.maxspeed:
                self.speed = self.maxspeed
            if self.speed <= -self.maxspeed:
                self.speed = -self.maxspeed

    def update(self):
        # 조작과 이동
        self.control()
        self.move()

        # 현재 방향에 따라 현재 이미지 변경
        self.image = self.images[self.direction]

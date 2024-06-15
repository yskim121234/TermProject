import pygame as pg
import numpy as np
from numba import *
from Character.Car import Car

SCREENWIDTH = 800
SCREENHEIGHT = 600

def Race():
    # pygame 초기화
    pg.init()
    
    mixer = pg.mixer
    mixer.init()
    
    # 창 크기
    screen = pg.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

    # 틱
    clock = pg.time.Clock()

    # 해상도 세팅
    hres = 120
    halfvres = 100

    mod = hres/60
    posx, posy, rot = 0, 0, 0

    #폰트
    font = pg.font.SysFont(None, 30)

    # 프레임
    frame = np.random.uniform(0, 1, (hres, halfvres*2, 3))

    # 하늘 이미지
    sky = pg.image.load('./Asset/Object/Sky.png')
    sky = pg.surfarray.array3d(pg.transform.scale(sky, (360, halfvres*2)))

    # 땅 이미지
    floor = pg.surfarray.array3d(pg.image.load('./Asset/Object/Track.jpg'))

    # 자동차 스프라이트
    car = Car((SCREENWIDTH/2 - 150, 300))
    
    #스프라이트 그룹
    sprites = pg.sprite.Group(car)

    # 메인 루프
    running = True
    while running:
        # 이벤트
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                        running = False

        # 프레임 생성
        frame = new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod)

        # 화면 구성
        surf = pg.surfarray.make_surface(frame*255)
        surf = pg.transform.scale(surf, (800, 600))
        screen.blit(surf, (0, 0))

        # 창 이름에 프레임 표시    
        fps = int(clock.get_fps())
        pg.display.set_caption('-FPS : {0}'.format(fps))

        # 현재 속도 표시
        text = font.render('%.1f Km/h' %(np.abs(car.speed)), False, 'white', 'black')
        screen.blit(text, (350,570))

        text = font.render('X:%.1f  Y:%.1f R: %.1f' %(posx, posy, rot), False, 'white', 'black')
        screen.blit(text, (0, 30))
        # 스프라이트 업데이트 및 그리기
        sprites.update()
        sprites.draw(screen)

        # 화면 업데이트
        pg.display.update()

        # 플레이어 이동
        posx, posy, rot = movement(posx, posy, rot, clock.tick(), car)
    pg.quit()

def movement(posx, posy, rot, et , car):
    # 자동차의 속도와 방향
    speed = car.speed
    direction = car.direction
    # 자동차의 방향이 오른쪽을 향할 경우
    if direction == 1 or direction == 3:
        rot = rot + 0.0002* et * speed
    elif direction == 2:
        posx, posy = posx - (np.sin(rot) *0.001* et * speed), posy + (np.cos(rot) * 0.001 * et * speed)

    # 자동차의 방향이 왼쪽을 향할 경우
    if direction == 5 or direction == 7:
        rot = rot - 0.0002* et * speed
    elif direction == 6:
        posx, posy = posx + (np.sin(rot) *0.001* et * speed), posy - (np.cos(rot) * 0.001 * et * speed)

    # speed에 비례하여 이동
    if direction == 0 or direction == 1 or direction == 7:
        posx, posy = posx + (np.cos(rot) *0.001* et * speed), posy + (np.sin(rot) * 0.001 * et * speed)
    elif 3<= direction <= 5:
         posx, posy = posx - (np.cos(rot) *0.001* et * speed), posy - (np.sin(rot) * 0.001 * et * speed)
    # 이동과 회전을 마친 좌표와 로테이션 리턴
    return posx, posy, rot

@njit() # 최적화
# 시점에 따른 새로운 프레임 생성
def new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod):
    for i in range(hres):
            # 수평 칙셀에 대해 현재 로테이션을 조정
            rot_i = rot + np.deg2rad(i/mod - 30)

            # 조정된 로테이션에 따른 각도 계산
            sin, cos = np.sin(rot_i), np.cos(rot_i)

            # 하늘 적용
            frame[i][:] = sky[int(np.rad2deg(rot_i)%359)][:]/255

            # 화면의 수직 절반
            for j in range(halfvres):
                # 거리 비율
                n = halfvres/(halfvres - j)

                # 바닥 텍스쳐의 좌표 계산
                x, y = posx + cos*n, posy + sin* n
                xx, yy = int(x*0.01%1*426), int(y*0.01%1*754)

                # 거리가 멀수록 어두워짐
                shade = 0.2 + 0.8* (1-j/halfvres)

                # 바닥 적용
                frame[i][halfvres*2-j-1] = shade * floor[xx][yy]/255
    # 만들어진 프레임 리턴
    return frame

if __name__ == '__main__':
    Race()
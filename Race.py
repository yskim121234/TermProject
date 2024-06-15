import pygame as pg
import numpy as np
from numba import *
from Character.Car import Car

SCREENWIDTH = 800
SCREENHEIGHT = 600

def Race():
    # pygame 초기화
    pg.init()
    
    # 창 크기
    screen = pg.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

    # 틱
    clock = pg.time.Clock()

    #
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

        text = font.render('X:%.1f  Y:%.1f' %(posx, posy), False, 'white', 'black')
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
        rot = rot + 0.0002* et * speed * 1.5

    # 자동차의 방향이 왼쪽을 향할 경우
    if direction == 5 or direction == 7:
        rot = rot - 0.0002* et * speed
    elif direction == 6:
        rot = rot - 0.0002* et * speed * 1.5

    # speed에 비례하여 이동
    posx, posy = posx + np.cos(rot) *0.001* et * speed, posy + np.sin(rot) * 0.001 * et * speed
        
    return posx, posy, rot

@njit()
def new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod):
    for i in range(hres):
            rot_i = rot + np.deg2rad(i/mod - 30)
            sin, cos = np.sin(rot_i), np.cos(rot_i)
            frame[i][:] = sky[int(np.rad2deg(rot_i)%359)][:]/255

            for j in range(halfvres):
                n = halfvres/(halfvres - j)
                x, y = posx + cos*n, posy + sin* n
                xx, yy = int(x*0.01%1*426), int(y*0.01%1*754)
                shade = 0.2 + 0.8* (1-j/halfvres)

                frame[i][halfvres*2-j-1] = shade * floor[xx][yy]/255
    return frame

if __name__ == '__main__':
    Race()
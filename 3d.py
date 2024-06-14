import pygame as pg
import numpy as np
from numba import *

def main():
    pg.init()
    screen = pg.display.set_mode((800,600))
    clock = pg.time.Clock()

    hres = 120
    halfvres = 100

    mod = hres/60
    posx, posy, rot = 0, 0, 0

    frame = np.random.uniform(0, 1, (hres, halfvres*2, 3))
    sky = pg.image.load('./Asset/Object/Sky.png')
    sky = pg.surfarray.array3d(pg.transform.scale(sky, (360, halfvres*2)))
    floor = pg.surfarray.array3d(pg.image.load('./Asset/Object/Grass.png'))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        frame = new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod)

        surf = pg.surfarray.make_surface(frame*255)
        surf = pg.transform.scale(surf, (800, 600))
        fps = int(clock.get_fps())
        pg.display.set_caption('-FPS : {0}'.format(fps))
        screen.blit(surf, (0, 0))
        pg.display.update()
        posx, posy, rot = movement(posx, posy, rot, pg.key.get_pressed(), clock.tick())


def movement(posx, posy, rot, keys, et):
    if keys[pg.K_a]:
        rot = rot - 0.005* et
    if keys[pg.K_d]:
        rot = rot + 0.005* et
    if keys[pg.K_w]:
        posx, posy = posx + np.cos(rot) *0.005* et, posy + np.sin(rot) * 0.005 * et
    if keys[pg.K_s]:
        posx, posy = posx - np.cos(rot) *0.005* et, posy - np.sin(rot) * 0.005 *et
        
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
                xx, yy = int(x*2%1*100), int(y*2%1*100)
                shade = 0.2 + 0.8* (1-j/halfvres)

                frame[i][halfvres*2-j-1] = shade * floor[xx][yy]/255
    return frame
main()
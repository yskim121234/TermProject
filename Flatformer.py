import pygame as pg
from Character.Charcter import Character
from Object.Platform import Platform
from Object.Goal import Goal
from Object.Lock import Lock
from Object.Key import Key
from Object.Background import Sky


# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

def Flatformer():
    pg.init()
    #Set screen
    size = [1280, 720]
    screen = pg.display.set_mode(size)

    #Loop option
    running = True
    clock = pg.time.Clock()

    sky = Sky(0, 0, 1280, 720)
    player = Character(position=(100, 420))
    platforms = [Platform(i*100, 620, 100, 100) for i in range(13)]
    goal = Goal(1120,420, 150, 200, [player])
    lock = Lock(goal)
    key = Key(720,220, 100, 100, [player], goal)

    all_sprites = pg.sprite.Group(sky, platforms, goal, lock, key, player)

    font = pg.font.SysFont(None, 30)
    #main loop
    while running:
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    Flatformer()
                if event.key == pg.K_ESCAPE:
                    running = False

        screen.fill(BLACK)
        
        pg.display.set_caption('FPS: %d' %(int(clock.get_fps())))

        if player.clear == True:
            gameclear = font.render("Game Clear", False, WHITE)
            rect = gameclear.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(gameclear, rect)

            gameclear = font.render("Press 'R' restart game", False, WHITE)
            rect = gameclear.get_rect()
            rect.center = screen.get_rect().center
            rect.center = [rect.centerx, rect.centery+20]
            screen.blit(gameclear, rect)
        else:
            keys = pg.key.get_pressed()
        

            all_sprites.update()
            all_sprites.draw(screen)

        pg.display.update()
        clock.tick(60)
    pg.quit()
    
if __name__ == '__main__':
    Flatformer()
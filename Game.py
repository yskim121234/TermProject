import pygame
from Charcter.Charcter import Character
from Object.Platform import Platform
from Object.Goal import Goal
from Object.Lock import Lock
from Object.Key import Key
from Object.Background import Sky
pygame.init()

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

def main():
    #Set Window
    size = [1280, 720]
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Title')

    #Loop option
    done = False
    clock = pygame.time.Clock()

    sky = Sky(0, 0, 1280, 720)
    player = Character(position=(100, 420))
    platforms = [Platform(i*100, 620, 100, 100) for i in range(13)]
    goal = Goal(1120,420, 150, 200, [player])
    lock = Lock(goal)
    key = Key(720,220, 100, 100, [player], goal)

    all_sprites = pygame.sprite.Group(sky, platforms, goal, lock, key, player)

    font = pygame.font.SysFont(None, 30)
    #main loop
    while not done:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_ESCAPE:
                    quit()

        window.fill(BLACK)

        if player.clear == True:
            gameclear = font.render("Game Clear", False, WHITE)
            rect = gameclear.get_rect()
            rect.center = window.get_rect().center
            window.blit(gameclear, rect)

            gameclear = font.render("Press 'R' restart game", False, WHITE)
            rect = gameclear.get_rect()
            rect.center = window.get_rect().center
            rect.center = [rect.centerx, rect.centery+20]
            window.blit(gameclear, rect)
        else:
            keys = pygame.key.get_pressed()

            

            all_sprites.update()
            all_sprites.draw(window)

        pygame.display.update()
        clock.tick(60)
    
if __name__ == '__main__':
    main()
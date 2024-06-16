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

def Platformer():
    pg.init()
    pg.mixer.init()
    # 창 설정
    size = [1280, 720]
    screen = pg.display.set_mode(size)

    # 옵션
    running = True
    clock = pg.time.Clock()

    # 배경
    sky = Sky(0, 0, 1280, 720)
    # 플레이어 객체 생성
    player = Character(position=(100, 420))
    # 바닥 객체 생성
    platforms = [Platform(i*100, 620, 100, 100) for i in range(13)]
    # 목적지 객체 생성
    goal = Goal(1120,420, 150, 200, [player])
    # 자물쇠 객체 생성 & 목적지 잠구기
    lock = Lock(goal)
    # 열쇠 객체 생성 & 플레이어 등록 & 목적지 등록
    key = Key(720,220, 100, 100, [player], goal)

    # 스프라이트 그룹 등록
    all_sprites = pg.sprite.Group(sky, platforms, goal, lock, key, player)

    # 폰트 객체 생성
    font = pg.font.SysFont(None, 30)

    #main loop
    while running:
        
        # 이벤트 루프
        for event in pg.event.get():
            # 종료
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                # R을 눌러 재시작
                if event.key == pg.K_r:
                    Platformer()
                # ESC를 눌러 종료
                if event.key == pg.K_ESCAPE:
                    running = False

        # 검은색으로 채우기
        screen.fill(BLACK)
        
        # 프레임을 제목으로 설정하여 초당 프레임 표시
        pg.display.set_caption('FPS: %d' %(int(clock.get_fps())))

        # 게임 클리어시
        if player.clear == True:
            # 게임 클리어 메시지
            gameclear = font.render("Game Clear", False, WHITE)

            # 메시지 중앙으로 옮기기
            rect = gameclear.get_rect()
            rect.center = screen.get_rect().center

            # 메시지 표시
            screen.blit(gameclear, rect)

            # 재시작 설명
            restart = font.render("Press 'R' restart game", False, WHITE)

            # 중앙으로
            rect = restart.get_rect()
            rect.center = screen.get_rect().center

            # 20 pixel 만큼 내리고
            rect.center = [rect.centerx, rect.centery+20]

            # 설명 표시
            screen.blit(restart, rect)
        else:
            # 모든 스프라이트 업데이트
            all_sprites.update()

            # 모든 스프라이트 그리기
            all_sprites.draw(screen)

        # 화면 업데이트
        pg.display.update()

        # 틱
        clock.tick(60)
    
    # pygame 종료
    pg.quit()
    
if __name__ == '__main__':
    Platformer()
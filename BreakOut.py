import pygame as pg
from Object.Ball import *
from Object.Pad import Pad
from Object.Brick import Brick
from Object.Nickname_Entry import Nickname_input
from Object.Difficulty_Option import Diff_Option
from Object.Heart import Heart
import tkinter.messagebox as mb
import numpy as np
import sqlite3

def Recode_Update(name, score):
    db = sqlite3.connect('./Recode.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS recode(name TEXT, score INT)""")
    cur.execute("""INSERT INTO recode (name, score) VALUES (?, ?)""", (name, score))
    db.commit()
    db.close()

def Recode_Load():
    recode = {}
    try:
        db = sqlite3.connect('./Recode.db')
        cur = db.cursor()
        cur.execute("""SELECT * FROM recode""")

        for tuple in cur:
            recode[tuple[1]] = tuple[0]
        db.close()
    except Exception as ex:
        mb.showerror('DB Error', str(ex)+ ' error')

        recode['Error'] = 'Error'
    finally:
        return recode

def BreakOut():
    #초기화
    pg.init()
    pg.display.init()
    pg.mixer.init()
    #화면 세팅
    pg.display.set_caption("Break Out")
    display = pg.display.set_mode([600, 800])

    # 게임 실행 변수 초기화
    running = True
    clock = pg.time.Clock()

    # 패드 생성 및 초기화
    pad = Pad(0, 765, 200, 25)
    pad.Max_Range_X = display.get_width()

    # 공 생성 및 초기화
    ball = Ball(25, 0, 0)

    # 벽돌 리스트 선언
    bricks = pg.sprite.Group()

    balls = pg.sprite.Group(ball)
    pad_sprite = pg.sprite.Group(pad)
    # 스코어 보드 설정 및 변수 초기화
    font = pg.font.SysFont(None, 30)
    score = 0
    recode = {}

    # 시작
    title = True
    # 체력 리스트 및 아이콘 생성
    health = pg.sprite.Group()
    for i in range(3):
        health.add(Heart(5 + 2.5 * i + 10 * i, 30))

    # 스테이지 관련 변수 초기화
    stage = 0
    clear = True

    # 닉네임 입력
    nickname_input = Nickname_input()

    # 난이도 선택
    difficulty_option = Diff_Option(display.get_width()/2 + 50,display.get_height()/2)

    difficulty = 1

    ######
    DB_Once = True
    #게임 루프
    while running:
        # 초당 100번의 Tick
        clock.tick(100)

        mouseX, mouseY = pg.mouse.get_pos()
        # 이벤트 루프
        for event in pg.event.get():
            # 윈도우의 X 버튼을 눌렀을 경우
            if event.type == pg.QUIT:
                running = False
            else:      
                if event.type == pg.MOUSEBUTTONDOWN:
                    if title:
                        if difficulty_option.Easy_Rect.Is_Hoverd(mouseX, mouseY) and pg.mouse.get_pressed()[0] == 1:
                            ball.Base_Speed = 5
                            difficulty = 1
                            difficulty_option.Easy_Rect.Clicked = True
                            difficulty_option.Hard_Rect.Clicked = False
                        if difficulty_option.Hard_Rect.Is_Hoverd(mouseX, mouseY) and pg.mouse.get_pressed()[0] == 1:
                            ball.Base_Speed = 10
                            difficulty = 2
                            difficulty_option.Hard_Rect.Clicked = True
                            difficulty_option.Easy_Rect.Clicked = False

                # 키가 눌렸을 경우
                if event.type == pg.KEYDOWN:
                    # 그 키가 ESC일 경우
                    if event.key == pg.K_ESCAPE:
                        running = False
                    if event.key == pg.K_BACKSPACE:
                        nickname_input.text = nickname_input.text[:-1]
                    elif len(nickname_input.text) < 8 and event.key != pg.K_RETURN and event.key != pg.K_SPACE and title == True:
                        nickname_input.text += event.unicode
                    if event.key == pg.K_RETURN:
                        title = False
                        del difficulty_option
                    if event.key == pg.K_r and title == False:
                        BreakOut()
                    
        # 화면을 검은색으로 채운다.
        display.fill('black')

        if title == True:
            nickname_input.Render(display, (display.get_width()/2 - nickname_input.rect.w/2), (display.get_height()/2) - 75)
            difficulty_option.Draw(display)
            desc1 = font.render("Enter your nickname and select difficulty.", True, 'white')
            desc2 = font.render("Press Enter to title", True, 'white')
            display.blit(desc1, ((display.get_width()/2) - desc1.get_rect().w/2, (display.get_height()/2) + 100))
            display.blit(desc2, ((display.get_width()/2) - desc2.get_rect().w/2, (display.get_height()/2) + 130))
        # 체력이 0보다 큰 경우
        elif len(health.sprites()) > 0:
            # 벽돌 갯수가 0보다 큰 경우
            if len(bricks.sprites()) <= 0:
                clear = True
                ball.Is_Ready = True
            
            # 공이 준비 상태인 경우
            if ball.Is_Ready:
                ball.Reset(pad)
            
            # 스테이지를 클리어한 경우
            if clear == True:
                # 다음 스테이지
                stage += 1
                ball.Base_Speed = 5 * difficulty * (1+ stage/10)
                # 벽돌 배치
                for i in range(4+stage):
                    for j in range(4+stage):
                        width = display.get_width()/(4+stage)
                        height = (display.get_height()/4+stage)/4
                        bricks.add(Brick(i*width, j*height, width, height))
                # 변수 초기화
                clear = False
            
            #충돌했을 경우
            hit_list = pg.sprite.groupcollide( balls, pad_sprite, False, False )
            for hitted in hit_list.keys():
                
                # 공이 충돌한 위치에 따라 튕겨지는 방향이 정해지는 방식
                # 공과 패드 중앙 사이의 거리
                distance_from_center = hitted.rect.centerx - pad.rect.centerx
                # 패드 절반 너비
                pad_width_half = pad.rect.w/2
                # 패드 중앙과의 거리 퍼센트 => 반사각 비율 (100% = 80도)
                reflection_ratio = distance_from_center/pad_width_half
                # 반사각
                if hitted.rect.centerx < pad.rect.centerx:
                    reflection_angle = np.radians(-15+ reflection_ratio * (80 - 15))
                elif hitted.rect.centerx > pad.rect.centerx:
                    reflection_angle = np.radians(15+ reflection_ratio * (80 - 15))

                hitted.Speed_X = hitted.Base_Speed * np.sin(reflection_angle)
                hitted.Speed_Y = -hitted.Base_Speed * np.cos(reflection_angle)

                if pg.mixer.get_busy:
                    pg.mixer.stop()
                pg.mixer.Sound('./Asset/Object/Ball/Bounce.wav').play()

            hit_list = pg.sprite.groupcollide(balls, bricks, False, True)
            for hitted in hit_list.keys():
                #공의 좌표가 벽돌의 가로 범위에 포함될 경우
                #=> 공이 위나 아래에서 충돌 되었을 경우
                overlapped = hit_list[hitted][0]
                if hitted.rect.centerx > overlapped.rect.x and hitted.rect.centerx < overlapped.rect.x + overlapped.rect.w:
                    hitted.Speed_Y = -hitted.Speed_Y
                #=> 공이 왼쪽이나 오른쪽에서 충돌 되었을 경우
                else:
                    hitted.Speed_X = -hitted.Speed_X

                if pg.mixer.get_busy:
                    pg.mixer.stop()
                pg.mixer.Sound('./Asset/Object/Ball/Bounce.wav').play()
                # 점수 증가
                score += (1 * 1 + (stage-1)/10)
            # 죽었을 경우
            if len(balls.sprites()) <= 0:
                healths = health.sprites()
                healths[-1].kill()
                if pg.mixer.get_busy:
                    pg.mixer.stop()
                pg.mixer.Sound('./Asset/Object/Ball/Dead.wav').play()
                ball = Ball(25, 0, 0)
                ball.Base_Speed = 5 * difficulty * (1+ stage/10)
                balls.add(ball)

            bricks.update()
            bricks.draw(display)

            balls.update()
            balls.draw(display)


            pad_sprite.update()
            pad_sprite.draw(display)

            health.update()
            health.draw(display)

            score = int(score)
            scoreboard = font.render('Score : %d' %(score), True, 'white', None)
            display.blit(scoreboard, (0,0))
            
        else:     # 만약 체력이 0보다 작거나 같은 경우
            if DB_Once == True:
                if nickname_input.text != None and nickname_input.text != '':     
                    Recode_Update(nickname_input.text, score)
                recode = Recode_Load()
                DB_Once = False
                scoreboard = [font.render(
                                recode[each_recode] + ' : ' + str(each_recode),
                                True,
                                'white',
                                None) for each_recode in sorted(recode.keys(), reverse= True)]

                if not list(recode.keys())[0] == "Error":
                    if float(sorted(recode.keys(), reverse= True)[0]) <= score:
                        mb.showinfo('Congratulations', message="You've achieved your best score!")

            # 중앙 좌표 설정
            x = (display.get_width()/2) - 100
            y = (display.get_height()/2) - 150

            # text 출력
            for i in range(6):
                if i >= len(scoreboard):
                    break
                display.blit(scoreboard[i], (x, y + (i*50)))

        # 화면 업데이트
        pg.display.update()
        pg.display.flip()
    pg.quit()
if __name__ == '__main__':
    BreakOut()
import pygame as pg
from Character.Animation import Animation

# 캐릭터 상태 매크로
IDLE = 0
WALK = 1
RUN  = 2

class Character(pg.sprite.Sprite):

    def __init__(self, position):
        super(Character, self).__init__()
        # 사이즈
        self.size = (200, 200)
        
        # X 이동 방향
        self.direction = 0

        # 애니메이션 리스트
        self.animations = []
        # 대기 애니메이션
        self.animations.append(Animation('./Asset/Character/Girl/Idle', self.size))
        # 걷기 애니메이션
        self.animations.append(Animation('./Asset/Character/Girl/Walk', self.size))
        
        # 상태 초기화
        self.idle()

        # Rect 생성
        self.rect = pg.Rect(position, self.size)

        # 현재 이미지 인덱스
        self.index = 0
        # 현재 이미지
        self.image = self.animations[IDLE].image

        # 이동 속도
        self.speed = 5

        # 점프 중인가?
        self.is_jumping = False
        # 기본 점프 속도
        self.movey = 20

        # 레벨 클리어 여부
        self.clear = False

    def control(self):
        # 입력 중인 키보드 키 리스트
        keys = pg.key.get_pressed()
        
        # 스페이스바를 눌렀다면
        if keys[pg.K_SPACE]:
                # 점프 함수
                self.jump()

        # 입력한 방향이 있다면
        if keys[pg.K_a] - keys[pg.K_d] != 0:
            # 걷기 함수의 인수를 입력에 따라 다르게 넣어줌
            self.walk(keys[pg.K_d] - keys[pg.K_a])

        # 입력한 방향이 없다면
        else:
            # 대기 함수
            self.idle()

    def update(self):
        # 조작   
        self.control()

        # 걷기 상태라면
        if self.state == WALK:
            # 방향과 속도에 따라 좌표 변경
            self.rect.x += self.direction * self.speed
        
        # 점프 중이라면    
        if self.is_jumping:
            # 점프 속도 만큼 좌표 변경
            self.rect.y -= self.movey

            # 점프 속도는 매번 줄어듦
            self.movey -= 1

            # 점프 속도가 -20 미만이라면
            if self.movey < -20:
                # 점프 끝
                self.is_jumping = False
                # 점프 속도 초기화
                self.movey = 20
            
            # 방향이 마이너스(왼쪽)라면
            if self.direction < 0:
                # 점프 이미지를 뒤집고 사이즈를 조절해서 현재 이미지로 설정
                self.image = pg.transform.flip(
                            pg.transform.scale(
                            pg.image.load('./Asset/Character/Girl/Jump/Jump (17).png'), self.size), True, False)
                # 함수 끝
                return
            # 방향이 0 이상(오른쪽)이라면 
            else:
                # 점프 이미지의 사이즈를 조절해서 현재 이미지로 설정
                self.image = pg.transform.scale(pg.image.load('./Asset/Character/Girl/Jump/Jump (17).png'), self.size)
                # 함수 끝
                return
        
        # 방향이 마이너스(왼쪽)라면
        if self.direction < 0:
            # 현재 상태(대기, 걷기)의 현재 프레임의 이미지를 뒤집어서 현재 이미지로 설정
            self.image = pg.transform.flip(self.animations[self.state].update(), True, False)
            return
        
        # 방향이 0 이상(오른쪽)이라면 
        else:
            # 현재 상태(대기, 걷기)의 현재 프레임의 이미지를 현재 이미지로 설정
            self.image = self.animations[self.state].update()

    def idle(self):
        # 현재 상태를 대기로 변경
        self.state = IDLE

    def walk(self, direction):
        
        # 만약 방향이 0이라면
        if direction == 0:
            # 아무것도 하지 않음
            return
        
        # 현재 상태를 걷기로 변경
        self.state = WALK
        
        # 현재 방향 설정
        self.direction = direction
        
    def jump(self):
        if self.is_jumping:
            return
        
        pg.mixer.Sound('./Asset/Character/Girl/Jump.wav').play()
        # 점프
        self.is_jumping = True
        
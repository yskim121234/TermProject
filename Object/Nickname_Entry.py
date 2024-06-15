import pygame as pg
class Nickname_input():
    def __init__(self):
        # 폰트 객체 생성
        self.font = pg.font.Font(None, 32)
        # 텍스트 초기화
        self.text = ''
        # Rect 생성
        self.rect = pg.Rect(0, 0,140, 32)
        # 색
        self.rect_color = pg.Color("white")

    def Render(self, surface, x, y):
        # 텍스트 서페이스 생성
        self.text_surface = self.font.render(self.text, True, (255,255,255))

        # 입력에 따라 Rect의 위치 설정
        self.rect.x = x
        self.rect.y = y

        # Rect의 너비를 (텍스트 서페이스의 너비 + 10)으로 설정
        self.rect.w = self.text_surface.get_width() + 10
        
        # 테두리 그리기
        pg.draw.rect(surface, self.rect_color, self.rect, 2)

        # 텍스트 그리기
        surface.blit(self.text_surface, (x+5, y+5))
    

       

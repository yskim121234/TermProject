import pygame as pg
from Object.Click_Rect import Click_Rect

class Diff_Option():
    def __init__(self, x, y):
        # 좌표 설정
        self.x = x - 100
        self.y = y

        # 폰트 설정
        self.font = pg.font.Font(None, 32)

        # 쉬움 버튼
        self.Easy_Rect = Click_Rect(self.x-75, self.y, 100, 75)
        self.Easy_Rect.Color = pg.Color(100,255,100)
        self.Easy_Rect.Clicked_Color = pg.Color(0, 155, 0)

        # 어려움 버튼
        self.Hard_Rect = Click_Rect(self.x+75, self.y, 100, 75)
        self.Hard_Rect.Color = pg.Color(255,0,0)
        self.Hard_Rect.Clicked_Color = pg.Color(155,0,0)
    
    def Draw(self, surface):
        # 쉬움 텍스트 생성
        Text_Easy = self.font.render('Easy', True, (255,255,255))

        # 쉬움이 클릭되었다면
        if self.Easy_Rect.Clicked:
            # 클릭된 색상의 버튼 그리기
            pg.draw.rect(surface, self.Easy_Rect.Clicked_Color, self.Easy_Rect)
        else:
            # 기본 색상의 버튼 그리기
            pg.draw.rect(surface, self.Easy_Rect.Color, self.Easy_Rect)
        # 그 위에 텍스트 그리기
        surface.blit(Text_Easy, (self.Easy_Rect.x+5, self.Easy_Rect.y+5))

        # 어려움 텍스트 생성
        Text_Hard = self.font.render('Hard', True, (255,255,255))

        # 어려움이 클릭되었다면
        if self.Hard_Rect.Clicked:
            # 클릭된 색상의 버튼 그리기
            pg.draw.rect(surface, self.Hard_Rect.Clicked_Color, self.Hard_Rect)
        else:
            # 기본 색상의 버튼 그리기
            pg.draw.rect(surface, self.Hard_Rect.Color, self.Hard_Rect)
        # 그 위에 텍스트 그리기
        surface.blit(Text_Hard, (self.Hard_Rect.x+5, self.Hard_Rect.y+5))
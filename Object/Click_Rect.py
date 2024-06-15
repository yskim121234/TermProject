import pygame as pg

class Click_Rect(pg.Rect):
    def __init__(self, x, y, w, h):
        super().__init__(int(x), int(y), w, h)

        # 색깔
        self.Color = pg.Color(255,255,255)

        # 클릭 시 색깔
        self.Clicked_Color = pg.Color(0,0,0)

        # 클릭되었는지
        self.Clicked = False
    
    def Is_Hoverd(self, mouseX, mouseY):
        # 마우스의 X 좌표가 버튼의 X 범위에 속하면서
        if mouseX <= self.x + self.w and self.x <= mouseX:
             # 마우스의 Y 좌표가 버튼의 Y 범위에 속하면
            if mouseY <= self.y + self.h and self.y <= mouseY:
                # True 리턴
                return True
        # 아니면 False 리턴
        return False
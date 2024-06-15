import pygame as pg

class Goal(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, players):
        super(Goal, self).__init__()

        # 사이즈
        size = (w, h)
        # 깃발 이미지 불러와서 사이즈 조절하여 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Flag.png'), size)
        
        # Rect 생성
        self.rect = pg.Rect(x, y, w, h)

        # 플레이어 등록
        self.players = players

        # 잠겨있는지
        self.locked = False

    def update(self):
        # 잠겨있다면
        if self.locked:
            # 아무것도 안함
            return

        # 플레이어와 충돌 시
        hit_players = pg.sprite.spritecollide(self, self.players, False)
        for p in hit_players:
            # 해당 캐릭터의 클리어 여부를 True로 변경
            p.clear = True
        
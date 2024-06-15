import pygame as pg

class Key(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, players, Object):
        super(Key, self).__init__()

        # 사이즈
        size = (w, h)

        # 키 이미지를 불러오고 사이즈를 조절해 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Key.png'), size)

        # Rect 생성
        self.rect = pg.Rect(x, y, w, h)

        # 플레이어 등록
        self.players = players

        # 잠금을 해제할 오브젝트 등록
        self.object = Object

    def update(self):
        # 플레이어와 충돌 시
        hit_players = pg.sprite.spritecollide(self, self.players, False)
        for p in hit_players:
            # 등록한 오브젝트의 잠금을 해제
            self.object.locked = False
            pg.mixer.Sound('./Asset/Object/Ball/HitPad.wav').play()
            # 스스로를 삭제
            self.kill()
        
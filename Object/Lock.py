import pygame as pg

class Lock(pg.sprite.Sprite):

    def __init__(self, Object):
        super(Lock, self).__init__()

        # 입력 받은 오브젝트를 잠굼
        Object.locked = True

        # 잠군 오브젝트 저장
        self.object = Object

        # 오브젝트의 Rect 저장
        self.rect = Object.rect

        # 오브젝트의 Rect에 따라 사이즈 수정
        size = (self.rect.w, self.rect.h)

        # 자물쇠 이미지 불러오고 사이즈를 수정해 저장
        self.image = pg.transform.scale(pg.image.load('./Asset/Object/Lock.png'), size)

    def update(self):
        # 등록한 오브젝트가 잠겨있다면
        if self.object.locked:
            # 아무것도 안함
            return
        # 스스로를 삭제
        self.kill()
        
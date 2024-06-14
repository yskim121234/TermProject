import pygame as pg

class Goal(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, players):
        super(Goal, self).__init__()

        size = (w, h)
        self.image = pg.image.load('./Asset/Object/Flag.png')
        self.image.convert_alpha()
        self.image.set_colorkey((0,255,0))
        self.rect = pg.Rect(x, y, w, h)
        self.image = pg.transform.scale(self.image, size)
        self.players = players
        self.locked = False

    def update(self):
        if self.locked:
            return
        hit_players = pg.sprite.spritecollide(self, self.players, False)
        for p in hit_players:
            p.clear = True
        
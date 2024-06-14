import pygame as pg

class Key(pg.sprite.Sprite):

    def __init__(self, x, y, w, h, players, Object):
        super(Key, self).__init__()

        size = (w, h)
        self.image = pg.image.load('./Asset/Object/Key.png')
        self.image.convert_alpha()
        self.image.set_colorkey((0,255,0))
        self.rect = pg.Rect(x, y, w, h)
        self.image = pg.transform.scale(self.image, size)
        self.players = players
        self.object = Object

    def update(self):
        hit_players = pg.sprite.spritecollide(self, self.players, False)
        for p in hit_players:
            self.object.locked = False
            self.kill()
        
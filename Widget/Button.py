import pygame as pg

class Button():
    def __init__(self, pos, size) -> None:
        self.rect = pg.Rect(pos, size)
        
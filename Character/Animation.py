import pygame as pg
import os

class Animation():
    def __init__(self, Image_Folder_Path, size) -> None:
        self.images = []
        for image in sorted(os.listdir(Image_Folder_Path)):
            self.images.append(
                pg.transform.scale(
                    pg.image.load('%s/%s' %(Image_Folder_Path, image)), size
                )
            )
        self.index = 0
        self.image = self.images[self.index]
        self.running = True

    def update(self):
        if self.running:
            self.index += 1

            # loop animation
            if self.index >= len(self.images):
                self.index = 0
            return self.images[self.index]
    
    def run(self):
        self.running = True

    def stop(self):
        self.running = False
        
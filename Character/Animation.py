import pygame as pg
import os
import tkinter.messagebox as mb

class Animation():

    def __init__(self, Image_Folder_Path, size) -> None:
        # 이미지 리스트
        self.images = []

        # 폴더 내의 모든 이미지의 크기를 조절하여 이미지 리스트에 저장
        try:
            for image in sorted(os.listdir(Image_Folder_Path)):
                self.images.append(
                    pg.transform.scale(
                        pg.image.load('%s/%s' %(Image_Folder_Path, image)), size))
        except Exception as ex:
            mb.showerror('Load image Error', 'Error type: %s' %(ex))
            
        # 현재 이미지의 인덱스
        self.index = 0
        
        # 현재 이미지
        self.image = self.images[self.index]

        # 애니메이션 재생 여부
        self.running = True

    def update(self):
        # 재생 중이라면
        if self.running:
            # 다음 이미지 
            self.index += 1

            # 애니메이션 루프
            if self.index >= len(self.images):
                self.index = 0

            # 새로 적용될 이미지 리턴
            return self.images[self.index]
    
    def run(self):
        # 재생
        self.running = True

    def stop(self):
        # 정지
        self.running = False
        
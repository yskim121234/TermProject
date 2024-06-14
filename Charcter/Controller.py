import pygame as py

class Controller():
    def __init__(self):
        self.Pressed = []
    
    def update(self):
        try:
            self.Pressed = py.key.get_pressed()
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    
    c = Controller()
    c.update()
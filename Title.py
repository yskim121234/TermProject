from tkinter import *
import Platformer
import Race
import BreakOut

def Pass():
    pass

def main():
    def start_game():
        games[select.get()]()

    app = Tk()
    app.title('텀프로젝트 -게임 모음- 20244033 김연성')
    app.geometry('400x200+320+180')
    app.config(bg='black')

    options = ['[3D] 레이스', '[2D] 벽돌깨기', '[2D] 플렛포머']
    games = {}
    games['게임을 선택하세요.'] = Pass
    games['[3D] 레이스'] = Race.Race
    games['[2D] 플렛포머'] = Platformer.Flatformer
    games['[2D] 벽돌깨기'] = BreakOut.BreakOut

    select = StringVar()
    select.set('게임을 선택하세요.')
    OptionMenu(app, select, *options).place(x= 125, y = 50, width= 150)

    Button(app, text='게임 시작', command=start_game).place(x=100,y=100,width=200,height=50)
    app.mainloop()

if __name__ == "__main__":
    main()
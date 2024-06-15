from tkinter import *
import Flatformer
import Race
import BreakOut

def Pass():
    pass
def start_game():
    games[select.get()]()

app = Tk()
app.title('텀프로젝트 -게임 모음- 20244033 김연성')
app.geometry('1280x720+320+180')
app.config(bg='black')

options = ['[3D] 레이스', '[2D] 벽돌깨기', '[2D] 플렛포머']
games = {}
games['게임을 선택하세요.'] = Pass
games['[3D] 레이스'] = Race.Race
games['[2D] 플렛포머'] = Flatformer.Flatformer
games['[2D] 벽돌깨기'] = Flatformer.BreakOut

select = StringVar()
select.set('게임을 선택하세요.')
OptionMenu(app, select, *options).place(x= 440, y = 50, width= 150)

Button(app, text='게임 시작', command=start_game).place(x=440,y=570,width=200,height=50)
app.mainloop()
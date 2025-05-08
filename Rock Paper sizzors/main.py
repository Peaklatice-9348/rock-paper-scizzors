import random
from tkinter import *
import tkinter.font as font
choises = ['rock','paper','scizzors']
win = 'IDK'
score = 0
def result(choice):
    global score
    choice2 = random.choice(choises)
    if choice2 == 'rock':
        if choice == 'paper':
            win = False
        if choice == 'scizzors':
            win = True

    if choice2 == 'paper':
        if choice == 'scizzors':
            win = False
        if choice == 'rock':
            win = True

    if choice2 == 'scizzors':
        if choice == 'rock':
            win = False
        if choice == 'paper':
            win = True

    if choice == choice2:
            win = 'IDK'
            cb.configure(bg='dark blue')
            wb.configure(text='Draw')

    if win == True:
        score += 1
        cb.configure(bg='dark green')
        wb.configure(text='You Win!')

    elif win == False:
        score -= 1
        cb.configure(bg='dark red')
        wb.configure(text='You lose :(')

    cb2.configure(text=f'{choice2}')
    cb.configure(text=f'{choice}')
    wwb.configure(text=f'score = {score}')

gui = Tk()

gui.title('Rock Paper Sizzors')
gui.configure(bg='black')

message = Label(gui,text='Rock, Paper or Scizzors',bg='grey',font=font.Font(size=120),width=21,height=2)
message.grid(row=1,column=1,columnspan=3)

cb = Label(gui,text='',bg='black',font=font.Font(size=120),width=7,height=2)
cb.grid(row=4,column=2)

cb2 = Label(gui,text='',bg='grey',font=font.Font(size=120),width=7,height=2)
cb2.grid(row=4,column=1)

whb = Label(gui,text='your choise',bg='dark grey',font=font.Font(size=20),width=41)
whb.grid(row=3,column=2)

whb2 = Label(gui,text='their choise',bg='dark grey',font=font.Font(size=20),width=41)
whb2.grid(row=3,column=1)

wwb = Label(gui,text='',bg='gold',font=font.Font(size=20),width=41)
wwb.grid(row=3,column=3)

wb = Label(gui,text='',bg='yellow',font=font.Font(size=60),width=14,height=4)
wb.grid(row=4,column=3)

rb = Button(gui,text='Rock',bg='dark grey',font=font.Font(size=120),width=7,height=2,command=lambda:result('rock'))
rb.grid(row=2,column=1)

pb = Button(gui,text='paper',bg='white',font=font.Font(size=120),width=7,height=2,command=lambda:result('paper'))
pb.grid(row=2,column=2)

sb = Button(gui,text='Scizzors',bg='silver',font=font.Font(size= 120),width=7,height=2,command=lambda:result('scizzors'))
sb.grid(row=2,column=3)

gui.mainloop()

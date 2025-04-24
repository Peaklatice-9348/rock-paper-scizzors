import random
from tkinter import *
import tkinter.font as font
def result(choice):
    pass

gui = Tk()
gui.title('Rock Paper Sizzors')
gui.configure(bg='grey')
message = Label(gui,text='Rock, Paper or Scizzors',bg='grey',font=font.Font(size=120),width=21,height=2)
message.grid(row=1,column=1,columnspan=3)
rb = Button(gui,text='Rock',bg='dark grey',font=font.Font(size=120),width=7,height=2,command=lambda:result('rock'))
rb.grid(row=2,column=1)
pb = Button(gui,text='paper',bg='white',font=font.Font(size=120),width=7,height=2,command=lambda:result('paper'))
pb.grid(row=2,column=2)
sb = Button(gui,text='Scizzors',bg='silver',font=font.Font(size= 120),width=7,height=2,command=lambda:result('scizzors'))
sb.grid(row=2,column=3)
gui.mainloop()
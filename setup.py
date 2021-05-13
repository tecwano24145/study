from tkinter import *

def hello():
    print('hello world')

win = Tk();
win.title('hello world')
win.geometry('200x100')

btn = Button(win,text='hello',command=hello)
btn.pack(expand=YES,fill=BOTH)

mainloop()
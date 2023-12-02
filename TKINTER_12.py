# place
from tkinter import *

window = Tk()


window.geometry('500x500')

button = Button(window,text='Button', width = 12)
button.place(x=250,y=250)

mainloop()
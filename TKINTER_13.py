# calculator 1

from tkinter import *

window = Tk()


window.geometry('500x500')

# entry box
e= Entry(window,width =56,borderwidth=5)
e.place(x=0,y=0)


# buttons

def click(num):
    result= e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))

b= Button(window, text = '1', width =12)
b.place(x=10,y=60)
b= Button(window, text = '2', width =12)
b.place(x=100,y=60)
b= Button(window, text = '3', width =12)
b.place(x=190,y=60)
b= Button(window, text = 'X', width =12)
b.place(x=280,y=60)



b= Button(window, text = '4', width =12)
b.place(x=10,y=110)
b= Button(window, text = '5', width =12)
b.place(x=100,y=110)
b= Button(window, text = '6', width =12)
b.place(x=190,y=110)
b= Button(window, text = '-', width =12)
b.place(x=280,y=110)


b= Button(window, text = '7', width =12)
b.place(x=10,y=160)
b= Button(window, text = '8', width =12)
b.place(x=100,y=160)
b= Button(window, text = '9', width =12)
b.place(x=190,y=160)
b= Button(window, text = '+', width =12)
b.place(x=280,y=160)




b= Button(window, text = '00', width =12)
b.place(x=10,y=210)
b= Button(window, text = '0', width =12)
b.place(x=100,y=210)
b= Button(window, text = '.', width =12)
b.place(x=190,y=210)
b= Button(window, text = '/', width =12)
b.place(x=280,y=210)



b= Button(window, text = 'clear', width =24)
b.place(x=10,y=260)
b= Button(window, text = '=', width =24)
b.place(x=190,y=260)
mainloop()
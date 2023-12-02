# calculator 3
# calculator 2
# adding function to the operator
from tkinter import *

window = Tk()


window.geometry('180x310')

# entry box
e= Entry(window,width =24,borderwidth=15)
e.place(x=0,y=0)


# buttons

def click(num):
    result= e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(num))







def MULTI():
    n1=e.get()
    global math
    math = 'multiplication'
    global i
    i = int(n1)
    e.delete(0,END)

# FIRST LINE OF THE CALULATOR

b= Button(window, text = '1',  width =4,height=2, command=lambda:click(1))
b.place(x=10,y=60)
b= Button(window, text = '2', width =4,height=2,command=lambda:click(2))
b.place(x=50,y=60)
b= Button(window, text = '3',  width =4,height=2,command=lambda:click(3))
b.place(x=90,y=60)
b= Button(window, text = 'X',  width =4,height=2,command=MULTI)
b.place(x=130,y=60)







# operators :-
def SUB():
    n1=e.get()
    global math
    math = 'substraction'
    global i
    i = int(n1)
    e.delete(0,END)

# SECOND LINE OF THE CALULATOR
b= Button(window, text = '4',  width =4,height=2,command=lambda:click(4))
b.place(x=10,y=110)
b= Button(window, text = '5',  width =4,height=2,command=lambda:click(5))
b.place(x=50,y=110)
b= Button(window, text = '6',  width =4,height=2,command=lambda:click(6))
b.place(x=90,y=110)
b= Button(window, text = '-', width =4,height=2,command=SUB)
b.place(x=130,y=110)





def add():
    n1=e.get()
    global math
    math = 'addition'
    global i
    i = int(n1)
    e.delete(0,END)
# THIRD LINE OF THE CALULATOR
b= Button(window, text = '7',  width =4,height=2,command=lambda:click(7))
b.place(x=10,y=160)
b= Button(window, text = '8',  width =4,height=2,command=lambda:click(8))
b.place(x=50,y=160)
b= Button(window, text = '9',  width =4,height=2,command=lambda:click(9))
b.place(x=90,y=160)
b= Button(window, text = '+',  width =4,height=2,command=add)
b.place(x=130,y=160)







def div():
    n1=e.get()
    global math
    math ='division'
    global i
    i = int(n1)
    e.delete(0,END)
# FOURTH LINE OF THE CALULATOR
b= Button(window, text = '0', width =15, height =2,command=lambda:click(0))
b.place(x=10,y=210)
b= Button(window, text = '/', width =4,height=2,command=div)
b.place(x=130,y=210)






# FIFTH LINE OF THE CALULATOR

def clear():
    e.delete(0,END)

b= Button(window, text = 'clear', width =10, height =2, command=clear)
b.place(x=10,y=260)


def equal():
    n2=e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0,i+int(n2))
    elif math == 'substraction':
        e.insert(0,i-int(n2))
    elif math == 'division':
        e.insert(0,i/int(n2))
    elif math == 'multiplication':
        e.insert(0,i*int(n2))


b= Button(window, text = '=', width =10, height =2, command = equal)
b.place(x=90,y=260)
mainloop()

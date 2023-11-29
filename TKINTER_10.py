# message box 2
# message box inside the window
from tkinter import *

window=Tk()


window.geometry('500x1000')
# message = Message(window, text ="python")
# message.pack()


# var = StringVar()
# message = Message(window, textvariable= var, relief=RAISED, padx=20, pady=20)
# var.set("Welcome")

var= StringVar()
end_var = StringVar()

def insert():
    result= end_var.get()
    var.set(result)

message = Message(window, textvariable=var, relief= RAISED, pady=50, padx=50)
entry = Entry(window, textvariable= end_var)
button= Button(window, text="ok", command= insert )
message.pack()
entry.pack()
button.pack()


mainloop()



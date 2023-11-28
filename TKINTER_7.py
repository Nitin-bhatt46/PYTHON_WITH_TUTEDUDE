# menubar

from tkinter import *

window=Tk()


# menubar

menu =Menu(window)
file = Menu(menu, tearoff = 0 )
# tearoff = 1 than the menu bar can become a floating bar
file.add_command(label="New")
file.add_command(label="open")
file.add_command(label="save")
file.add_command(label="save as")
file.add_separator()

file.add_command(label="exit")

menu.add_cascade(label="File", menu = file)
window.config(menu=menu)

mainloop()
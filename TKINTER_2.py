# BASIC MODIFICATION USING TKINTER.


# step 1 : import tkinter


from tkinter import *


# step 2 :- GUI interaction

window = Tk()


# step 3 : adding inputs
# title naming
window.title("simple")
# geometery
window.geometry("500x700")
# background.
window.config(bg="Yellow")

inp = Label(window , text ="Nitin Hello 'welcome' to TKINTER")
inp.pack()


# step 4 : main loop

window.mainloop()
# Frames and buttons using tkinter


# step 1 : import tkinter


from tkinter import *


# step 2 :- GUI interaction

window = Tk()


# step 3 : adding inputs
# title naming
window.title("simple")
# geometery
window.geometry("1080x700")
# background.
window.config(bg="Yellow")

# creatng frame
frame1= Frame(window, bg ="red", width = 300, height = 300, cursor="dot")
frame2= Frame(window, bg ="green", width = 300, height = 300,cursor="circle")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

# creating frame

button1= Button(frame1, text="Press",bg="blue", fg="white")
button1.pack()



inp = Label(window , text ="Nitin Hello 'welcome' to TKINTER")
inp.pack()

# step 4 : main loop

window.mainloop()
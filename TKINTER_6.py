# handling buttons

from tkinter import *

#2
window =Tk()


#3
window.title("welcome")
window.geometry("500x600")
def log_entry():
    print("already Logged in")

button = Button(window, text="LOGIN", command = log_entry, width = 12, bg="red",  fg="white", font=("bold,12"), activebackground="black",activeforeground="white")
button.pack()


#4
mainloop()
# message box


from tkinter import *
import tkinter.messagebox

window=Tk()


tkinter.messagebox.showerror(title="hurry",message="Running out of time")
question =tkinter.messagebox.askyesno("Weather",message="Will it rain ?" )

if question == True:
    print("use umbrella")
else:
    print("bye go")
mainloop()
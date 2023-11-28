# pack

from tkinter import *


# step 2
window = Tk()

 # step3
window.title("welcome")
window.geometry("500x500")

label1= Label(window, text="Label-1", bg="red", fg="white")
label1.pack(side=TOP, fill=X, expand=False)

label2= Label(window, text="Label-2", bg="blue", fg="white")
label2.pack(side=LEFT, fill=Y, expand=False)

label3= Label(window, text="Label-3", bg="green", fg="white")
label3.pack(side=BOTTOM, fill=X, expand=False)

label4= Label(window, text="Label-4", bg="BLACK", fg="white")
label4.pack(side=RIGHT, fill=Y, expand=False)


# EXPAND = TRUE THE LABEL COME TO MIDDLE.

# step 4
mainloop()
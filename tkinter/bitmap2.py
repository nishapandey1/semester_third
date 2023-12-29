from tkinter import *

root = Tk()

root.geometry("700x700")

bitmaps = ["warning",

           "gray75",

           "gray50",

           "gray25",

           "gray12",

           "hourglass",

           "info",

           "questhead",

           "question",

           "error"]

for bit in bitmaps:

    Button(root, relief=RAISED, bitmap=bit).pack(pady=10)

root.mainloop()


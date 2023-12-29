#Menu driven Using Tkinter

from tkinter import *
root=Tk()
root.geometry("600x700")
root.title("Menu")
txt=Text(root,bg="lightyellow")
txt.pack()

def info1():
    output="this is info1.\n"
    txt.insert(END, output)
def info2():
    output="this is info2.\n"
    txt.insert(END, output)
def info3():
    output="this is info3."
    txt.insert(END, output)
def close():
    root.destroy()

mymenu=Menu(root)
mymenu.add_command(label="File",command=info1)
mymenu.add_command(label="Edit",command=info2)
mymenu.add_command(label="View",command=info3)
mymenu.add_command(label="Exit", command=close)

root.config(menu=mymenu)
root.mainloop()

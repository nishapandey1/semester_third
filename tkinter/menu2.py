from tkinter import *

root=Tk()

root.geometry("800x600")

root.title("ProgramMenu")

txt = Text(root,bg="gray")

txt.pack()

def file():

    output="This is a file menu\n"

    txt.insert(END, output)

def edit():

    output="This is an edit menu\n"

    txt.insert(END, output)

def selection():

    output="This is a selection menu\n"

    txt.insert(END, output)

def view():

    output="This is a View menu\n"

    txt.insert(END, output)

def go():

    output="This is a Go menu\n"

    txt.insert(END, output)

def run():

    output="This is a Run menu\n"

    txt.insert(END, output)

def terminal():

    output="This is a Terminal menu\n"

    txt.insert(END, output)

def help():

    output="This is a Help menu\n"

    txt.insert(END, output)

def exit():

    root.destroy()

def clearwindow():

    txt.delete("1.0",END)



mymenu=Menu(root)


mymenu.add_command(label="File",command=file)

mymenu.add_command(label="Edit",command=edit)

mymenu.add_command(label="Selection",command=selection)

mymenu.add_command(label="View",command=view)

mymenu.add_command(label="Go",command=go)

mymenu.add_command(label="Run",command=run)

mymenu.add_command(label="Terminal",command=terminal)

mymenu.add_command(label="Help",command=help)

mymenu.add_command(label="Exit",command=exit)

root.config(menu=mymenu)

Button(text="clear",command=clearwindow).pack()

root.mainloop()
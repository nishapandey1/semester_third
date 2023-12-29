from tkinter import *
root=Tk()
root.geometry("800x700")
root.title("Menu")

txt=Text(root,bg="black",fg="white")
txt.pack()

def new():
    output="This is new\n"
    txt.insert(END, output)

def newwindow():
    output="This is new window\n"
    txt.insert(END, output)

def open():
    output="This is open\n"
    txt.insert(END, output)


def save():
    output="This is save\n"
    txt.insert(END, output)


def saveAs():
    output="This is Save As\n"
    txt.insert(END, output)


def print():
    output="This is print\n"
    txt.insert(END, output)


def printsetup():
    output="This is printsetup\n"
    txt.insert(END, output)

def cut():
    output="This is cut\n"
    txt.insert(END, output)

def paste():
    output="This is paste\n"
    txt.insert(END, output)

def copy():
    output="This is copy\n"
    txt.insert(END, output)

def find():
    output="This is dfind\n"
    txt.insert(END, output)

def replace():
    output="This is replace\n"
    txt.insert(END, output)

def goto():
    output="This is goto\n"
    txt.insert(END, output)

def zoom():
    output="This is zoom\n"
    txt.insert(END, output)

def statusbar():
    output="This is statusbar\n"
    txt.insert(END, output)

def wordwrap():
    output="This is wordwrap\n"
    txt.insert(END, output)

def clear():
    txt.delete("1.0",END)

mainmenu=Menu(root)
filemenu=Menu(mainmenu, tearoff=0, bg="gray")
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="New Window", command=newwindow)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Print", command=print)
filemenu.add_command(label="Page Setup", command=printsetup)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

mainmenu.add_cascade(label="File", menu=filemenu)

editmenu=Menu(mainmenu, tearoff=0, bg="gray")
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_command(label="Find",command=find)
editmenu.add_command(label="Replace",command=replace)
editmenu.add_command(label="Go to",command=goto)

mainmenu.add_cascade(label="Edit", menu=editmenu)

viewmenu=Menu(mainmenu, tearoff=0, bg="gray")
viewmenu.add_command(label="Zoom",command=zoom)
viewmenu.add_command(label="Status bar",command=statusbar)
viewmenu.add_command(label="word wrap",command=wordwrap)

mainmenu.add_cascade(label="View", menu=viewmenu)


Button(text="clear",command=clear).pack()

root.config(menu=mainmenu)
root.mainloop()
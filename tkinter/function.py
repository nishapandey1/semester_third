import messagebox
from tkinter import *
root=Tk()

def info():
    messagebox.showinfo("This is Title", "It displays the context")
root.geometry("700x700")
a=Button(root,text="Click Me", command=info)
a.pack()
b=Button(text="close", command=root.destroy)
b.pack()
root.mainloop()


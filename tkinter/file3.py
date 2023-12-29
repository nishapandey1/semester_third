from tkinter import *
root=Tk()
root.geometry("700x700")
a=Button(text="Click Me", relief=RAISED, font=("Algerian",18), bg="Gray", fg="Black")
a.grid(column=1, row=2)
b=Button(text="close",font=("Algerian",18), command=root.destroy)
b.grid(column=3, row=2)

root.mainloop()
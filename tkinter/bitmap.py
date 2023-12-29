from tkinter import *

root=Tk()

root.geometry("800x800")

# Button(bitmap="error",relief=RAISED).pack(pady=15)

# Button(bitmap="questhead").pack(pady=15)

# Button(bitmap="question").pack(anchor="ne",pady=15)

Button(root,text="error",relief=SUNKEN, bitmap="error").pack(pady=15)

Button(root,text="hourglass",relief=RAISED ,bitmap="hourglass").pack(pady=15)

Button(root,text="info",relief=FLAT ,bitmap="info").pack(pady=15)

Button(root,text="question",relief=GROOVE ,bitmap="question" ).pack(pady=15)

Button(root,text="warning",relief=RIDGE,bitmap="warning").pack(pady=15)

Button(root,text="questhead",relief=SOLID, bitmap="questhead").pack(pady=15)

Button(root,text="questhead",relief=RAISED, bitmap="questhead").pack(pady=15)

Button(root,text="gray75",relief=RAISED ,bitmap="gray75").pack(pady=15)

Button(root,text="gray50",relief=RAISED ,bitmap="gray50").pack(pady=15)

Button(root,text="gray25",relief=RAISED ,bitmap="gray25" ).pack(pady=15)

Button(root,text="gray12",relief=RAISED,bitmap="gray12").pack(pady=15)



root.mainloop()


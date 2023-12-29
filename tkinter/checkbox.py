from tkinter import *
root=Tk()

def close():
    root.destroy()


root.geometry("700x600")
root.title("Form")
Label(root,text="First Name").grid(row=1)
Label(root,text="Last Name").grid(row=2)
Entry(root).grid(row=1,column=1)
Entry(root).grid(row=2,column=1)

Label(root,text="Hobbies", font=("Times New Roman",18,"bold")).grid(row=3)
var1=IntVar()
var2=IntVar() 
var3=IntVar()
var4=IntVar()

Checkbutton(root,text="Photography",variable=var1).grid(row=4,sticky=W)
Checkbutton(root,text="Travelling",variable=var2).grid(row=5,sticky=W)
Checkbutton(root,text="Reading MAnga",variable=var3).grid(row=6,sticky=W)
Checkbutton(root,text="Videography",variable=var4).grid(row=7,sticky=W)

var5=IntVar()

Label(root,text="Gender",font=("Times New Roman",18,"bold")).grid(row=8)
Radiobutton(root,text="Male",variable=var5,value=1).grid(row=9,sticky=W)
Radiobutton(root,text="Female",variable=var5,value=2).grid(row=10,sticky=W)
Radiobutton(root,text="Other",variable=var5,value=3).grid(row=11,sticky=W)


Button(root,text="Close Form",bg="gray",command=close).grid(row=16)
mainloop()
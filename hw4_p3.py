import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("400x600")
root.title("CSE 337 Drawing Program")

# make some of the widgets
cmd = IntVar()
canvas = Canvas(master, width=400, height=400)
p1 = Label(root, text="Command:")
e1  = Entry(root, width=40)
p2  = Label(root, text="value")
e2  = Entry(root, width=40)
p3  = Label(root, text="value")
e3  = Entry(root, width=40)
p4  = Label(root, text="value")
e4  = Entry(root, width=40)

ve  = Text(root, width=40, height=5)

def doRadio():
    c = cmd.get() # get the command number
    if c == 1: # search with a given name
        canvas.create_rectangle(int(e1.get(), e2.get(), e3.get(), e4.get()))
    elif c == 2: # insert a (name, phone number) record
        canvas.create_line(int(e1.get(), e2.get(), e3.get(), e4.get()))
    else: # delete the record with given name
        canvas.create_oval(int(e1.get(), e2.get(), e3.get(), e4.get()))

#finish making widgets
r1=Radiobutton(root,text="Rectangle",variable=cmd,value=1,command=doRadio)
r2=Radiobutton(root,text="Line",variable=cmd,value=2,command=doRadio)
r3=Radiobutton(root,text="Oval",variable=cmd,value=3,command=doRadio)

# pack
canvas.pack()
p1.pack()
e1.pack()
p2.pack()
e2.pack()
p3.pack()
e3.pack()
p4.pack()
e4.pack()
r1.pack()
r2.pack()
r3.pack()


# loop over main program, save database after user quits
root.mainloop()


import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("400x600")
root.title("CSE 337 Drawing Program")

# make some of the widgets
cmd = IntVar()
color = IntVar()
canvas = Canvas(root, width=400, height=400)
p1 = Label(root, text="P1")
e1  = Entry(root, width=40)
p2  = Label(root, text="P2")
e2  = Entry(root, width=40)
p3  = Label(root, text="P3")
e3  = Entry(root, width=40)
p4  = Label(root, text="P4")
e4  = Entry(root, width=40)

ve  = Text(root, width=40, height=5)

def doRadio():
    c = cmd.get() # get the command number
    colorOption = color.get()
    if c == 1: # search with a given name
        if colorOption == 4:
            canvas.create_rectangle(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='blue')
        elif colorOption == 5:
            canvas.create_rectangle(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='green')
        elif colorOption == 6:
            canvas.create_rectangle(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='red')
        else:
            canvas.create_rectangle(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='white', outline='black')
    elif c == 2: # insert a (name, phone number) record
        if colorOption == 4:
            canvas.create_line(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='blue', outline='blue')
        elif colorOption == 5:
            canvas.create_line(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='green', outline='green')
        elif colorOption == 6:
            canvas.create_line(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='red', outline='red')
        else:
            canvas.create_line(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='white', outline='black')
        #canvas.create_line(int(e1.get(), e2.get(), e3.get(), e4.get()))
    else: # delete the record with given name
        if colorOption == 4:
            canvas.create_oval(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='blue')
        elif colorOption == 5:
            canvas.create_oval(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='green')
        elif colorOption == 6:
            canvas.create_oval(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='red')
        else:
            canvas.create_oval(int(e1.get()), int(e2.get()), int(e3.get()), int(e4.get()), fill='white', outline='black')
        #canvas.create_oval(int(e1.get(), e2.get(), e3.get(), e4.get()))

#finish making widgets
r1=Radiobutton(root,text="Rectangle",variable=cmd,value=1,command=doRadio)
r2=Radiobutton(root,text="Line",variable=cmd,value=2,command=doRadio)
r3=Radiobutton(root,text="Oval",variable=cmd,value=3,command=doRadio)

# color radio buttons
r4=Radiobutton(root,text="Blue",variable=color,value=4)
r5=Radiobutton(root,text="Green",variable=color,value=5)
r6=Radiobutton(root,text="Red",variable=color,value=6)

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
r4.pack()
r5.pack()
r6.pack()

# loop over main program, save database after user quits
root.mainloop()
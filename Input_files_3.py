from tkinter import *

root = Tk()

Entry = Entry(root, width=58)
Entry.pack()
Entry.insert(0, "Enter your name")

def myClick():
    hello = "Hello " + Entry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Done", command=myClick)
myButton.pack()

root.mainloop()
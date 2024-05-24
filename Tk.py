from tkinter import *

root = Tk()

e = Entry(root, width=100, borderwidth=2)
e.pack()
e.insert(0, "Enter Your god damn name: ")

def myClick():
    hello = "Hello " + e.get() + " you dumb mf"
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Click me bitch", padx=50, pady=100, command=myClick)
myButton.pack()

root.mainloop()

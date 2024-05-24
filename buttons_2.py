from tkinter import *

root = Tk()

def myClick():
    myLabel1 = Label(root, text="Look! I clicked a Button!", fg="red", bg="blue")
    myLabel1.pack()
    

# Creating a widget
myButton = Button(root, text="My button!", command=myClick)
# Shoving it onto the screen
myButton.pack()

root.mainloop()
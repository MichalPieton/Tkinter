from tkinter import *

root = Tk()
# Creating a Label Widget
myLabel1 = Label(root, text = "Siema")
myLabel2 = Label(root, text = "Elo")
# Shoving it onto the screen
myLabel1.grid(row= 0, column= 0)
myLabel2.grid(row= 1, column= 0)

root.mainloop()
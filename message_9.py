from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hello world")
root.iconbitmap("photo/rose.ico")


def popup():
    response = messagebox.showinfo("This is my Popup!", "Hello world!")
    Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()


root.mainloop()
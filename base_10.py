from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello world")
root.iconbitmap("photo/rose.ico")

def open():
    global my_img
    top = Toplevel()
    top.title("Hello world")
    top.iconbitmap("photo/rose.ico")
    my_img = ImageTk.PhotoImage(Image.open("photo/dog.jpeg"))
    my_label = Label(top, image=my_img).pack()
    button_exit = Button(top, text="EXIT PROGRAM", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()


root.mainloop()
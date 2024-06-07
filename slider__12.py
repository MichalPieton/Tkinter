from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Hello world")
root.iconbitmap("photo/rose.ico")

vertical = Scale(root, from_=0, to=400, orient=VERTICAL)
vertical.pack()

 
def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get())) 

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Click me!", command=slide).pack()

root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title("Hello world")
root.iconbitmap("photo/rose.ico")
 
 
def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="photo", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Openm File XS", command=open).pack()

root.mainloop()
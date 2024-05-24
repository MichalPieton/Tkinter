from tkinter import *
from PIL import ImageTk, Image


root = Tk()

root.iconbitmap('C:\\Users\\WHK478\\Desktop\\pythong\\Tk\\photo\\rose.ico')

frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click here!")
b.pack()

root.mainloop()
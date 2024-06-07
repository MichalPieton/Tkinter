from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hello world")
root.iconbitmap("photo/rose.ico")

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel1 = Label(root, text=value)
    myLabel1.pack()
    
def popup(value):
    messagebox.showinfo("This is my Popup!", value)
                  

myButton = Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()
Button(root, text="Popup", command=lambda: popup(pizza.get())).pack()

root.mainloop()
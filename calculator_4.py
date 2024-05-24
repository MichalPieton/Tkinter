from tkinter import *

root = Tk()

def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
    
def add_button():
    global char
    char = '+'
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def subtract_button():
    global char
    char = '-'
    first_number = e.get() 
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def multiply_button():
    global char
    char = '*'
    first_number = e.get() 
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def divide_button():
    global char
    char = '/'
    first_number = e.get() 
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)
    
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if char == '+':
        e.insert(0, f_num + int(second_number))
    elif char == '-':
        e.insert(0, f_num - int(second_number))
    elif char == '*':
        e.insert(0, f_num * int(second_number))
    elif char == '/':
        e.insert(0, round(f_num / int(second_number), 2))

# Define text_box
e = Entry(root, width=35, borderwidth=5)

# Define buttons
Button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

Button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

Button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

Button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
Button_add = Button(root, text="+", padx=39, pady=20, command=add_button)
Button_equal = Button(root, text="=", padx=87, pady=20, command=lambda: button_equal())
Button_clear = Button(root, text="Clear", padx=77, pady=20, command=lambda: button_clear())

Button_subtract = Button(root, text="-", padx=41, pady=20, command=subtract_button)
Button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply_button)
Button_divide = Button(root, text="/", padx=41, pady=20, command=divide_button)


# Solution box
e.grid(row=0,  column=0, columnspan=3, padx=10, pady=10)

# Put the buttons on the screen
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)

Button0.grid(row=4, column=0)
Button_clear.grid(row=4, column=1, columnspan=2)
Button_add.grid(row=5, column=0)
Button_equal.grid(row=5, column=1, columnspan=2)

Button_subtract.grid(row=6, column=0)
Button_multiply.grid(row=6, column=1)
Button_divide.grid(row=6, column=2)


root.mainloop()















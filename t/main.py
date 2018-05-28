from tkinter import *
from tkinter import ttk

root = Tk()

entry_value = StringVar(root, value="")

def button_press(self, value):
    print(value)
# Define title for the app
root.title("Calculator")

# Defines the width and height of the window
root.geometry("630x220")

# Block resizing of Window
# root.resizable(width=False, height=False)

# Customize the styling for the buttons and entry
style = ttk.Style()
style.configure("TButton",
                font="Serif 15",
                padding=10)

style.configure("TEntry",
                font="Serif 18",
                padding=10)

# Create the text entry box
number_entry = ttk.Entry(root,
                              textvariable=entry_value, width=50)
number_entry.grid(row=0, columnspan=4)

# ----- 1st Row -----

button7 = ttk.Button(root, text="7", command=lambda: button_press('7')).grid(row=1, column=0)

button8 = ttk.Button(root, text="8", command=lambda: button_press('8')).grid(row=1, column=1)

button9 = ttk.Button(root, text="9", command=lambda: button_press('9')).grid(row=1, column=2)
button10 = ttk.Button(root, text="/", command=lambda: button_press('9')).grid(row=1, column=2)

# button_div = ttk.Button(root, text="/", command=lambda: b('/')).grid(row=1, column=3)

# ----- 2nd Row -----

button4 = ttk.Button(root, text="4", command=lambda: button_press('4')).grid(row=2, column=0)

button5 = ttk.Button(root, text="5", command=lambda: button_press('5')).grid(row=2, column=1)

button6 = ttk.Button(root, text="6", command=lambda: button_press('6')).grid(row=2, column=2)
button16 = ttk.Button(root, text="6", command=lambda: button_press('6')).grid(row=2, column=2)

# button_mult = ttk.Button(root, text="*", command=lambda: math_button_press('*')).grid(row=2, column=3)

# ----- 3rd Row -----

button1 = ttk.Button(root, text="1", command=lambda: button_press('1')).grid(row=3, column=0)

button2 = ttk.Button(root, text="2", command=lambda: button_press('2')).grid(row=3, column=1)

button3 = ttk.Button(root, text="3", command=lambda: button_press('3')).grid(row=3, column=2)
button13 = ttk.Button(root, text="3", command=lambda: button_press('3')).grid(row=3, column=2)

# button_add = ttk.Button(root, text="+", command=lambda: math_button_press('+')).grid(row=3, column=3)

# ----- 4th Row -----

button_clear = ttk.Button(root, text="AC", command=lambda: button_press('AC')).grid(row=4, column=0)

button0 = ttk.Button(root, text="0", command=lambda: button_press('0')).grid(row=4, column=1)
button110 = ttk.Button(root, text="0", command=lambda: button_press('0')).grid(row=4, column=1)

# button_equal = ttk.Button(root, text="=", command=lambda: equal_button_press()).grid(row=4, column=2)

root.mainloop()
from tkinter import *
from tkinter import ttk

root = Tk()
def button_press(value):
    print(value)

root.title("FedUni Banking")
root.geometry("440x640")
root.rowconfigure(2, minsize=60)

# --------------- Collumn 1 -------------------------

header = ttk.Label(root, text="FedUni Banking", justify=CENTER, font = "Helvetica 32 bold").grid(
    columnspan=3, row=1, pady=25, padx=40)
entry_value_acc = StringVar(root, value="")
entry_value_pswd = StringVar(root, value="")

style = ttk.Style()

style.configure("TEntry",
                font="Serif 28"
                )


# --------------- Collumn 2 -------------------------
acc_label = ttk.Button(root, text="Account Number/ PIN", width=17, command=lambda: button_press('acc')).grid(
    ipady=37, sticky=W, row=2, column=0)

acc_entry = ttk.Entry(root, width=18, textvariable=entry_value_acc)
acc_entry.insert(END, "123456")
acc_entry.grid(row=2,  column=1, ipady=40, sticky=W)

acc_pswd = ttk.Entry(root, width=18, textvariable=entry_value_pswd, show="*")
acc_pswd.insert(END, "123456")
acc_pswd.grid(row=2,  column=2, ipady=40, sticky=W)


# --------------- Collumn 3 -------------------------
button1 = ttk.Button(root, text="1", width=17, command=lambda: button_press('1')).grid(
    ipady=40, sticky=W, row=3, column=0)

button2 = ttk.Button(root, text="2", width=17, command=lambda: button_press('2')).grid(
    ipady=40, sticky=W, row=3, column=1)

button3 = ttk.Button(root, text="3", width=17, command=lambda: button_press('3')).grid(
    ipady=40, sticky=W, row=3, column=2)

# --------------- Collumn 4 -------------------------
button4 = ttk.Button(root, text="4", width=17, command=lambda: button_press('4')).grid(
    ipady=40, sticky=W, row=4, column=0)

button5 = ttk.Button(root, text="5", width=17, command=lambda: button_press('5')).grid(
    ipady=40, sticky=W, row=4, column=1)

button6 = ttk.Button(root, text="6", width=17, command=lambda: button_press('6')).grid(
    ipady=40, sticky=W, row=4, column=2)

# --------------- Collumn 5 -------------------------
button7 = ttk.Button(root, text="7", width=17, command=lambda: button_press('7')).grid(
    ipady=40, sticky=W, row=5, column=0)

button8 = ttk.Button(root, text="8", width=17, command=lambda: button_press('8')).grid(
    ipady=40, sticky=W, row=5, column=1)

button9 = ttk.Button(root, text="9", width=17, command=lambda: button_press('9')).grid(
    ipady=40, sticky=W, row=5, column=2)


# --------------- Collumn 6 -------------------------

"""Configure the coloured buttons"""
ttk.Style().configure("cancel.TButton", foreground='black', background='red')
ttk.Style().configure("equal.TButton", foreground='black', background='green')

buttonClear = ttk.Button(root, text="Cancel/Clear", style="cancel.TButton", width=17, command=lambda: button_press('Clear')).grid(
    ipady=40, sticky=W, row=6, column=0)

button0 = ttk.Button(root, text="0", width=17, command=lambda: button_press('0')).grid(
    ipady=40, sticky=W, row=6, column=1)

buttonEqual = ttk.Button(root, text="Log In", style="equal.TButton", width=17, command=lambda: button_press('Login')).grid(
    ipady=40, sticky=W, row=6, column=2)


root.mainloop()


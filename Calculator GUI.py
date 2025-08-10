from tkinter import *

root = Tk()
root.title("Mera calc")

# Entry box:

entry = Entry(root, width=50, borderwidth=3, fg="black")
entry.grid(row=0, column=0, columnspan=4,)
place = int("0")


# Number button func:


operator = ""


def button_press(num):
    temp = entry.get()
    global operator

    if "+" in temp:
        operator = "+"
        entry.delete(0, END)

    elif "-" in temp:
        operator = "-"
        entry.delete(0, END)

    elif "*" in temp:
        operator = "*"
        entry.delete(0, END)

    elif "/" in temp:
        operator = "/"
        entry.delete(0, END)

    global place
    entry.insert(place, num)
    place += 1

# Function of all operators:


num1 = 0
second_num = ""


def add(op):
    first_num = float(entry.get())
    global num1
    if operator == "+":

        num1 = num1 + first_num
        entry.delete(0, END)
        entry.insert(0, op)

    else:
        num1 = first_num
        entry.delete(0, END)
        entry.insert(0, op)


def sub(op):
    first_num = float(entry.get())
    global num1
    if operator == "-":

        num1 = num1 - first_num
        entry.delete(0, END)
        entry.insert(0, op)

    else:
        num1 = first_num
        entry.delete(0, END)
        entry.insert(0, op)


def mul(op):

    first_num = float(entry.get())
    global num1
    if operator == "*":

        num1 = num1 * first_num
        entry.delete(0, END)
        entry.insert(0, op)

    else:
        num1 = first_num
        entry.delete(0, END)
        entry.insert(0, op)


def div(op):

    first_num = float(entry.get())
    global num1
    if operator == "/":

        num1 = num1 / first_num
        entry.delete(0, END)
        entry.insert(0, op)

    else:
        num1 = first_num
        entry.delete(0, END)
        entry.insert(0, op)


# Equal symbol func:


def equal():
    global second_num
    second_num = float(entry.get())
    entry.delete(0, END)

    if operator == "+":
        entry.insert(0, num1 + second_num)

    elif operator == "-":
        entry.insert(0, num1 - second_num)

    elif operator == "*":
        entry.insert(0, num1 * second_num)

    elif operator == "/":
        entry.insert(0, num1 / second_num)

# Clear button func:


def clear():
    entry.delete(0, END)
    global num1
    global second_num
    global operator
    num1 = 0
    second_num = 0
    operator = ""


# All numerical buttons:


button_1 = Button(root, text=1, padx=30, pady=10,
                  command=lambda: button_press(1))
button_1.grid(row=4, column=0)

button_2 = Button(root, text=2, padx=30, pady=10,
                  command=lambda: button_press(2))
button_2.grid(row=4, column=1)

button_3 = Button(root, text=3, padx=30, pady=10,
                  command=lambda: button_press(3))
button_3.grid(row=4, column=2)

button_4 = Button(root, text=4, padx=30, pady=10,
                  command=lambda: button_press(4))
button_4.grid(row=3, column=0)

button_5 = Button(root, text=5, padx=30, pady=10,
                  command=lambda: button_press(5))
button_5.grid(row=3, column=1)

button_6 = Button(root, text=6, padx=30, pady=10,
                  command=lambda: button_press(6))
button_6.grid(row=3, column=2)

button_7 = Button(root, text=7, padx=30, pady=10,
                  command=lambda: button_press(7))
button_7.grid(row=2, column=0)

button_8 = Button(root, text=8, padx=30, pady=10,
                  command=lambda: button_press(8))
button_8.grid(row=2, column=1)

button_9 = Button(root, text=9, padx=30, pady=10,
                  command=lambda: button_press(9))
button_9.grid(row=2, column=2)

button_0 = Button(root, text=0, padx=30, pady=10,
                  command=lambda: button_press(0))
button_0.grid(row=5, column=1,)

button_dot = Button(root, text=".", padx=31, pady=10,
                    command=lambda: button_press("."))
button_dot.grid(row=5, column=2)

# Clear button:

button_clear = Button(root, text="Clear", bg="orange",
                      fg="white", padx=95, pady=10, command=clear)
button_clear.grid(row=1, column=0, columnspan=3)

# Operator buttons:

button_add = Button(root, text="+", padx=31, pady=10,
                    command=lambda: add("+"))
button_add.grid(row=2, column=3)

button_sub = Button(root, text="-", padx=32, pady=10,
                    command=lambda: sub("-"))
button_sub.grid(row=3, column=3)

button_mul = Button(root, text="*", padx=32, pady=10,
                    command=lambda: mul("*"))
button_mul.grid(row=4, column=3)

button_div = Button(root, text="/", padx=32, pady=10,
                    command=lambda: div("/"))
button_div.grid(row=5, column=3)

# Equal button

button_equal = Button(root, text="=", padx=31, pady=10,
                      command=equal)
button_equal.grid(row=1, column=3)

root.resizable(False, False)
root.mainloop()

import math
from tkinter import *
import mp3play

root = Tk()
root.title = "Simple Calculator"
#Creates box that user can type in 
e = Entry(root, width=35, borderwidth=5, bg="grey", fg="white")
e.grid(row=0, column=0,columnspan=3, padx=10, pady=10)

root.config(background='green')

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) 

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
 
def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


f = mp3play.load('Beep.mp3'); play = lambda: f.play()
def play_sound():
    f.play()


#Define buttons
button_1 = Button(root, text="1", fg = 'green', padx=40, pady=20, command= lambda: [button_click(1),play_sound()])
button_2 = Button(root, text="2", fg = 'green', padx=40, pady=20, command= lambda: [button_click(2),play_sound()])
button_3 = Button(root, text="3", fg = 'green', padx=40, pady=20, command= lambda: [button_click(3),play_sound()])
button_4 = Button(root, text="4", fg = 'green', padx=40, pady=20, command= lambda: [button_click(4),play_sound()])
button_5 = Button(root, text="5", fg = 'green', padx=40, pady=20, command= lambda: [button_click(5),play_sound()])
button_6 = Button(root, text="6", fg = 'green', padx=40, pady=20, command= lambda: [button_click(6),play_sound()])
button_7 = Button(root, text="7", fg = 'green', padx=40, pady=20, command= lambda: [button_click(7),play_sound()])
button_8 = Button(root, text="8", fg = 'green', padx=40, pady=20, command= lambda: [button_click(8),play_sound()])
button_9 = Button(root, text="9", fg = 'green', padx=40, pady=20, command= lambda: [button_click(9),play_sound()])
button_0 = Button(root, text="0", fg = 'green', padx=40, pady=20, command= lambda: [button_click(0),play_sound()])
button_add = Button(root, text="+", padx=39, pady=20, command= button_add)
button_subtract = Button(root, text="-", padx=39, pady=20, command= button_subtract)
button_equal = Button(root, text="=", padx=39, pady=20, command= button_equal)
button_clear = Button(root, text="Clear", padx=88, pady=20, command= button_clear)
button_multiply = Button(root, text="*", padx=39, pady=20, command= button_multiply)
button_divide = Button(root, text="%", padx=39, pady=20, command= button_divide)


# Put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1 ,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1 ,column=2)
button_0.grid(row=4 ,column=0)
button_clear.grid(row=6, column=1, columnspan=2)
button_add.grid(row=4, column=1)
button_equal.grid(row=5, column=2)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)


root.mainloop()
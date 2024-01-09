from tkinter import *

root = Tk()
root.title("Calculator")
entry1 = Entry(root, width = 20, borderwidth = 5)
entry1.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady= 10)
def click(number):
  current = entry1.get()
  entry1.delete(0, END)
  entry1.insert(0, str(current) + str(number))
def clear():
  entry1.delete(0, END)
def add():
  first_number = entry1.get()
  entry1.delete(0, END)
  global f_num
  global math
  math = "addition"
  f_num = float(first_number)
def minus():
  first_number = entry1.get()
  entry1.delete(0, END)
  global f_num
  global math
  math = "subtraction"
  f_num = float(first_number)
def multiply():
  first_number = entry1.get()
  entry1.delete(0, END)
  global f_num
  global math
  math = "multiplication"
  f_num = float(first_number)
def divide():
  first_number = entry1.get()
  entry1.delete(0, END)
  global f_num
  global math
  math = "division"
  f_num = float(first_number)
def power():
  first_number = entry1.get()
  entry1.delete(0, END)
  global f_num
  global math
  math = "power"
  f_num = float(first_number)

def equal():
  second_number = entry1.get()
  entry1.delete(0, END)
  s_num = float(second_number)
  if math == "addition":
    answer = f_num + s_num
    entry1.insert(0, answer)
  elif math == "subtraction":
    answer = f_num - s_num
    entry1.insert(0, answer)
  elif math == "multiplication":
    answer = f_num * s_num
    entry1.insert(0, answer)
  elif math == "power":
    answer = f_num ** s_num
    entry1.insert(0, answer)
  else:
    answer = f_num / s_num
    entry1.insert(0, answer)

Button(root, text = "7", padx = 25, pady = 10, bg = "grey",command = lambda: click(7)).grid(row = 1,column = 0)
Button(root, text = "8", padx = 25, pady = 10,bg = "grey", command = lambda: click(8) ).grid(row = 1,column = 1)
Button(root, text = "9", padx = 25, pady = 10,bg = "grey", command = lambda: click(9)).grid(row = 1,column = 2)
Button(root, text = "6", padx = 25, pady = 10,bg = "grey", command = lambda: click(6)).grid(row = 2,column = 0)
Button(root, text = "5", padx = 25, pady = 10,bg = "grey", command = lambda: click(5)).grid(row = 2,column = 1)
Button(root, text = "4", padx = 25, pady = 10,bg = "grey", command = lambda: click(4)).grid(row = 2,column = 2)
Button(root, text = "3", padx = 25, pady = 10,bg = "grey", command = lambda: click(3)).grid(row = 3,column = 0)
Button(root, text = "2", padx = 25, pady = 10,bg = "grey", command = lambda: click(2)).grid(row = 3,column = 1)
Button(root, text = "1", padx = 25, pady = 10,bg = "grey", command = lambda: click(1)).grid(row = 3,column = 2)
Button(root, text = "0", padx = 25, pady = 10,bg = "grey", command = lambda: click(0)).grid(row = 4,column = 0)
Button(root, text = "π", padx = 25, pady = 10,bg = "grey",command = lambda: click(3.141)).grid(row = 4,column = 1)

Button(root, text = "Clear", padx = 45, pady = 10,bg = "orange",command = clear).grid(row = 6,column = 1,columnspan = 2)
Button(root, text = "+", padx = 25, pady = 10,bg = "orange", command = add).grid(row = 4,column = 2)
Button(root, text = "-", padx = 27, pady = 10,bg = "orange", command = minus).grid(row = 5,column = 2)
Button(root, text = "x", padx = 25, pady = 10,bg = "orange", command = multiply).grid(row = 5,column = 1)
Button(root, text = "^", padx = 25, pady = 10,bg = "orange", command = power).grid(row = 6,column = 0)
Button(root, text = "÷", padx = 25, pady = 10,bg = "orange", command = divide).grid(row = 5,column = 0)
Button(root, text = "=", padx = 90, pady = 10,bg = "orange", command = equal).grid(row = 7,column = 0,columnspan = 3)
root.mainloop()

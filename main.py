#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry("400x480")
root.resizable(width=False, height=False)
root.title("Calculator")

def btn1():
	val1 = valVar.get()+'1'
	notOk = True
	while notOk:
		if val1[0] == '0' and val1[1] == '.':
			notOk = False
		elif val1[0] == '0' and val1[1] != '.':
			val1 = val1[1:]
		elif val1[0] != '0':
			notOk = False
	valVar.set(val1)

def btn2():
	val2 = valVar.get()+'2'
	notOk = True
	while notOk:
		if val2[0] == '0' and val2[1] == '.':
			notOk = False
		elif val2[0] == '0' and val2[1] != '.':
			val2 = val2[1:]
		elif val2[0] != '0':
			notOk = False
	valVar.set(val2)

def btn3():
	val3 = valVar.get()+'3'
	notOk = True
	while notOk:
		if val3[0] == '0' and val3[1] == '.':
			notOk = False
		elif val3[0] == '0' and val3[1] != '.':
			val3 = val3[1:]
		elif val3[0] != '0':
			notOk = False
	valVar.set(val3)

def btn4():
	val4 = valVar.get()+'4'
	notOk = True
	while notOk:
		if val4[0] == '0' and val4[1] == '.':
			notOk = False
		elif val4[0] == '0' and val4[1] != '.':
			val4 = val4[1:]
		elif val4[0] != '0':
			notOk = False
	valVar.set(val4)

def btn5():
	val5 = valVar.get()+'5'
	notOk = True
	while notOk:
		if val5[0] == '0' and val5[1] == '.':
			notOk = False
		elif val5[0] == '0' and val5[1] != '.':
			val5 = val5[1:]
		elif val5[0] != '0':
			notOk = False
	valVar.set(val5)

def btn6():
	val6 = valVar.get()+'6'
	notOk = True
	while notOk:
		if val6[0] == '0' and val6[1] == '.':
			notOk = False
		elif val6[0] == '0' and val6[1] != '.':
			val6 = val6[1:]
		elif val6[0] != '0':
			notOk = False
	valVar.set(val6)

def btn7():
	val7 = valVar.get()+'7'
	notOk = True
	while notOk:
		if val7[0] == '0' and val7[1] == '.':
			notOk = False
		elif val7[0] == '0' and val7[1] != '.':
			val7 = val7[1:]
		elif val7[0] != '0':
			notOk = False
	valVar.set(val7)

def btn8():
	val8 = valVar.get()+'8'
	notOk = True
	while notOk:
		if val8[0] == '0' and val8[1] == '.':
			notOk = False
		elif val8[0] == '0' and val8[1] != '.':
			val8 = val8[1:]
		elif val8[0] != '0':
			notOk = False
	valVar.set(val8)

def btn9():
	val9 = valVar.get()+'9'
	notOk = True
	while notOk:
		if val9[0] == '0' and val9[1] == '.':
			notOk = False
		elif val9[0] == '0' and val9[1] != '.':
			val9 = val9[1:]
		elif val9[0] != '0':
			notOk = False
	valVar.set(val9)

def btn0():
	val0 = valVar.get()+'0'
	if val0[0] == '0' and val0[1] == '0':
		val0 = val0[1:]
	valVar.set(val0)

def reset():
	valVar.set("0")

valVar = tk.StringVar(root)
valVar.set("0")

# Results display Frame
display_lbl_frame = tk.LabelFrame(root)
display_lbl_frame.grid(row=0,column=0,columnspan=2,padx=10, pady=5)

display_label = tk.Entry(display_lbl_frame,font=('10'), textvariable=valVar,highlightthickness=5,bd=5,width=35, justify="right")
display_label.pack()

# Numbers Frame
nums_frame = tk.LabelFrame(root)
nums_frame.grid(row=1,column=0,sticky='N',padx=5,pady=5)

# Math Symbols Frame
math_sym_frame = tk.LabelFrame(root,pady=3)
math_sym_frame.grid(row=1,column=1,columnspan=1,sticky='N',padx=5,pady=5)

# 1,2,3
b1 = tk.Button(nums_frame, text='1',font=(12),padx=25,pady=25, command=btn1)
b1.grid(row=0,column=0,pady=2,padx=2)

b2 = tk.Button(nums_frame, text='2',font=(12),padx=25,pady=25, command=btn2)
b2.grid(row=0,column=1,pady=2,padx=2)

b3 = tk.Button(nums_frame, text='3',font=(12),padx=25,pady=25, command=btn3)
b3.grid(row=0,column=2,pady=2,padx=2)

# 4,5,6
b4 = tk.Button(nums_frame, text='4',font=(12),padx=25,pady=25, command=btn4)
b4.grid(row=1,column=0,pady=2,padx=2)

b5 = tk.Button(nums_frame, text='5',font=(12),padx=25,pady=25, command=btn5)
b5.grid(row=1,column=1,pady=2,padx=2)

b6 = tk.Button(nums_frame, text='6',font=(12),padx=25,pady=25, command=btn6)
b6.grid(row=1,column=2,pady=2,padx=2)

# 7,8,9
b7 = tk.Button(nums_frame, text='7',font=(12),padx=25,pady=25, command=btn7)
b7.grid(row=2,column=0,pady=2,padx=2)

b8 = tk.Button(nums_frame, text='8',font=(12),padx=25,pady=25, command=btn8)
b8.grid(row=2,column=1,pady=2,padx=2)

b9 = tk.Button(nums_frame, text='9',font=(12),padx=25,pady=25, command=btn9)
b9.grid(row=2,column=2,pady=2,padx=2)

# 0
b0 = tk.Button(nums_frame, text='0',font=(12),padx=96,pady=23, command=btn0)
b0.grid(row=3,column=0,columnspan=3,pady=2,padx=2)


def addition():
	addVar = valVar.get()+'+'
	valVar.set(addVar)

def subtraction():
	subVar = valVar.get()+'-'
	valVar.set(subVar)

def multiplication():
	multVar = valVar.get()+'*'
	valVar.set(multVar)

def division():
	divVar = valVar.get()+'/'
	valVar.set(divVar)

def dot():
	dotVar = valVar.get()
	dotVar += '.'
	valVar.set(dotVar)

def open_bracket():
	openBracketVar = valVar.get()
	operations = ['+','-','*','/']
	for operation_char in operations:
		if  openBracketVar[-1] == operation_char:
			openBracketVar += '('
		elif openBracketVar[-1] == '(':
			openBracketVar += '('
			break
		elif openBracketVar[-1].isnumeric():
			openBracketVar += '*('
			break
	valVar.set(openBracketVar)

def close_bracket():
	closeBracketVar = valVar.get() + ')'
	valVar.set(closeBracketVar)

def equals():
	eqVar = eval(valVar.get())
	valVar.set(eqVar)

def removeChar():
	removeVar = valVar.get()
	removeVar = removeVar[:-1]
	if len(removeVar) == 0:
		removeVar = '0'
	valVar.set(removeVar)

# Symbols Buttons
additionBtn = tk.Button(math_sym_frame, text = "+",font=(12),padx=25,pady=25, command=addition)
additionBtn.grid(row=0,column=0,padx=2,pady=2)

subtractionBtn = tk.Button(math_sym_frame, text = "-",font=('TkDefaultFont',12,'bold'),padx=25,pady=25, command=subtraction)
subtractionBtn.grid(row=0,column=1,padx=2,pady=2)

multiplicationBtn = tk.Button(math_sym_frame, text = "x",font=(12),padx=25,pady=25, command=multiplication)
multiplicationBtn.grid(row=1,column=0,padx=2,pady=2)

divisionBtn = tk.Button(math_sym_frame, text = ":",font=(12),padx=25,pady=25, command=division)
divisionBtn.grid(row=1,column=1,padx=2,pady=2)

open_bracketBtn = tk.Button(math_sym_frame, text= "(",font=(12), padx=25, pady=25, command=open_bracket)
open_bracketBtn.grid(row=2,column=0)

close_bracketBtn = tk.Button(math_sym_frame, text= ")",font=(12), padx=25, pady=25, command=close_bracket)
close_bracketBtn.grid(row=2,column=1)

dotBtn = tk.Button(math_sym_frame, text= ".",font=('TkDefaultFont',12,'bold'), padx=24, pady=22, command=dot)
dotBtn.grid(row=3,column=0,sticky='N',padx=2,pady=2)

delBtn = tk.Button(math_sym_frame, text= "<-",font=("TkDefaultFont",12,'bold'),padx=17,pady=22,command=removeChar)
delBtn.grid(row=3,column=1,sticky='N',padx=2,pady=2)

# Equal Frame
equalFrame = tk.LabelFrame(root)
equalFrame.grid(row=2,column=1,sticky='N')

equalsBtn = tk.Button(equalFrame, text = "=",font=("TkDefaultFont",12,'bold'), padx=58, pady=27, command=equals)
equalsBtn.grid(row=4,column=0,columnspan=2,padx=2,pady=2)

# Exit & Reset Frame
exit_frame = tk.LabelFrame(root)
exit_frame.grid(row=2)

resetBtn = tk.Button(exit_frame, text="Reset",bd=3,font=(12),padx=20,pady=25,command=reset)
resetBtn.grid(row=2,column=0,sticky='N',padx=8,pady=2)

exitBtn = tk.Button(exit_frame, text="Exit",font=(12),bd=3,padx=20,pady=25,command=root.destroy)
exitBtn.grid(row=2,column=1,sticky='N',padx=8,pady=2)

root.mainloop()

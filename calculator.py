from tkinter import *
from ArithmeticAnalizer import valid

"""
Tested with:
5+((1+2)*4)-3
20-(4+3)*2 
((3*3)-9)
(3*3)-9
3*3-9
03*3-9
003*003
(9-2)/7
9-2/7
2^3
(6+2)*3/2^2-4
"""

#####################################
symbols = ['(',')','%','^',
           '7','8','9','/',
           '4','5','6','*',
           '1','2','3','-',
           '0','AC','=','+']
rows = 5
cols = 4
hierarchy = {'^':0, '*':1, '/':1, '%':1, '+':2, '-':2}
#####################################

#ROOT
root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)

#FRAME
frame = Frame()
frame.pack()
frame.config(bg="black")

arithmetic = StringVar();

#ENTRY LABEL
inp = Entry(frame,bg="grey",bd=8,width=22, font=("Arial",15),
            state = "disabled", textvariable=arithmetic)
inp.grid(row=0,column=0,padx=10,pady=10,columnspan=4)


def op_condition(new,top,stack,expression):
    try:
        #If the new one has same priority, we take the top
        #print(f"new {new} --> {hierarchy[new]}  top {top} --> {hierarchy[top]}"
             # + f"{hierarchy[new] == hierarchy[top]}")
        if hierarchy[new] == hierarchy[top]:
            expression.append(stack.pop())
        #If the new one is less prioritary, we empty the stack
        elif hierarchy[new] > hierarchy[top]:
            while stack:
                expression.append(stack.pop())
            
    #The except happens when the new or top symbol is ( or )
    except:
        #When we find an end parenthesis, we have to take the
        # symbols between the two parenthesis
        if new == ')':
            last = stack.pop()
            while last != "(":
                expression.append(last)
                last = stack.pop()
            
    #Add the new element in the stack 
    finally:
        if new != ')':
            stack.append(new)
                        
#Change the notation from interfix to posfix to be interpretate by the calculator
def postfix(f):
    stack = []
    expression = []
    number = ""
    operation = ""

    for symbol in f:
        if '0' <= symbol <= '9':
            number += symbol
        else:
            #Adding one number if exists
            if number:
                expression.append(int(number))
                number = ""
                
            #Adding one symbol
            operation = symbol
            if stack:
                op_condition(operation,stack[len(stack)-1],stack,expression)
            else:
                stack.append(operation)
            #print(f"Exp-->{expression}")
            #print(f"Stack-->{stack}")

    #As the append is in the logic else, we need append
    # the last number
    if number:
        expression.append(int(number))

    #The list must be reversed in order to works like a stack
    expression.extend(stack[::-1])

    return expression

def operation(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "^":
        return a**b
    elif operator == "/":
        if b == 0:
            return "MATH ERROR"
        return a/b
    elif operator == "%":
        return a%b


def calculate(Fx):
    result = "INVALID EXPRESSION"
    Fx = Fx[::-1]
    aux_stack = []
    # #print(int(len(Fx)/2))
    #print(f" Partimos de :{Fx}")
    for digit in range(int(len(Fx))):
        # #print(f"-->{digit}")
        top = Fx.pop()
        aux_stack.append(top)
        # #print(Fx)
        if isinstance(top,str):
            op = aux_stack.pop()
            b = aux_stack.pop()
            a = aux_stack.pop()
            # #print(f"{a}{op}{b}")
            result = operation(a,b,op)
            
            aux_stack.append(result)
            
        
    return result

def think(f):
    if not valid(f)[0]:
       arithmetic.set("SYNTAX ERROR")
    else:
        expr = postfix(f)
        out = calculate(expr)
        if not isinstance(out,str):
            out = int(out)
        arithmetic.set(out)

#GUUI method
def type(symbol):
    if arithmetic.get() == "SYNTAX ERROR" or arithmetic.get() == "MATH ERROR" or arithmetic.get() == "INVALID EXPRESSION":
        arithmetic.set("")

    if symbol == "AC":
        arithmetic.set("")
    elif symbol == "=":
        think(arithmetic.get())
    elif not (symbol == "0" and not len(arithmetic.get())):
        arithmetic.set(arithmetic.get()+str(symbol))


buttons = []
for s in symbols:
    button = Button(frame, text=s, bg="grey",  font=("Arial",15), bd = 6,
              relief="raised", padx=2, pady=2, cursor = "hand2",
              highlightcolor="#8c8989", width="5", command = lambda symbol=s : type(symbol))
    buttons.append(button);


#Start in 1 bc in 0 we have the entry label
for r in range(1,rows+1):
    for c in range(cols):
        buttons[cols*(r-1)+c].grid(row=r,column=c)



root.mainloop()


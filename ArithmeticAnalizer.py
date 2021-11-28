oprs = ["+", "-", "*", "/", "=", "%", "*", "^"]

"""
Tested examples:
a+b
(a+b)
()
a(+b)
x**2+3
y***3
y=m*x+b
"""

def valid(f):
    #Empty string
    if not f:
        return (False,f"Empty arithmetic operation")
    #The exppression cannot start with an operator or )
    elif f[0] in oprs or f[0] == ')':
        return (False,"Not allowed star with an operator symbol")
    #The exppression cannot end with an operator or (
    elif f[len(f)-1] in oprs or f[len(f)-1] == '(':
        return (False,"Not allowed end with an operator symbol")
    else:
        #The program must have pair number of parenthesis
        paren = 0
            
        for i in range(len(f)-1):
            #if we find an open parenthesis...
            if f[i] == '(':
                paren += 1
                subf = ""
                #We should find its close parenthesis
                for j in range(i+1,len(f)):
                    if f[j] == ')':
                        #if we find it, repeat the proccess with the expreesion in the parents
                        if not valid(subf)[0]:
                            return (False,f"Incorrect syntax starting from position {i+1}")
                        break
                    #if we don't find the close parenthesis
                    elif j == len(f)-1:
                        return (False,f"Missing close parenthesis for position {i+1}")
                    
                    if f[j] != '(':
                        subf = subf + f[j]
            elif f[i] == ')':
                paren -= 1
                
            #The expression can't have two following operators, unless **
            elif f[i] in oprs and f[i+1] in oprs:
                if  not ( (f[i] == "*" and f[i+1] == "*") ^ (f[i] == "*" and f[i-1] == "*")):
                    return (False, f"Incorrect syntax in position {i+1}: '{f[i]}{f[i+1]}'")
        if f[len(f)-1] == ')':
            paren -= 1
    
    if paren:
         return (False,f"{abs(paren)} invalid parenthesis")
    return (True,"1")
                
def arithmetic_analizer(f):  
    if valid(f):
        id = []
        op = []
        for i in (range(len(f))):
            if f[i] != '(' and f[i] != ')':
                if f[i] not in oprs:
                    id.append(f[i])
                else:
                    if f[i] == "*":
                        if f[i+1] == "*":
                            op.append("**")
                        elif f[i-1] != "*":
                            op.append(f[i])
                    else:
                        op.append(f[i]) 
        
        print("The identifiers are: ")
        for i in id:
            print(i)
        print("The operators are: ")
        for i in op:
            print(i)
            
def main():
    f = input("Write one arithmetic expression:\t")  
    arithmetic_analizer(f)
    
if __name__ == "__main__":
    main()
            

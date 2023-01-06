from functools import *
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def fdiv(x,y):
    return x//y
def exp(x,y):
    return x**y
def modl(x,y):
    return x%y
l=[]
print("""Enter the following choice
    1 for addition
    2 for subtraction
    3 for multiplication
    4 for division
    5 for floor division
    6 for exponentiation
    7 for conversion  of decimal to binary
    8 for conversion of decimal to octal
    9 for conversion  of decimal to hexadecimal
    10 for modulo division
    11 for conversion of binary to octal
    12 for conversion of binary to hexadecimal
    13 for conversion of octal to hexadecimal
    14 for conversion of hexadecimal to octal
    """)
ch=int(input("Enter the choice"))
if(ch==1 or ch==2 or ch==3 or ch==4 or ch==5 or ch==6):
    n=int(input("Enter the number of input numbers"))
    for i in range(n):
        p=int(input("Enter the operand"))
        l.append(p)
    if(ch==1):
        s=reduce(add,l)
        print(s)
    elif(ch==2):
        s=reduce(sub,l)
        print(s)
    elif(ch==3):
        s=reduce(mul,l)
        print(s)
    elif(ch==4):
        s=reduce(div,l)
        print(s)
    elif(ch==5):
        s=reduce(fdiv,l)
        print(s)
    elif(ch==10):
        s=reduce(modl,l)
        print(s)
    else:
        s=reduce(exp,l)
        print(s)
elif(ch==7):
    n=int(input("Enter the number"))
    b=bin(n)
    print(b)
elif(ch==8):
    n=int(input("Enter the number"))
    o=oct(n)
    print(o)
elif(ch==9):
    n=int(input("Enter the number"))
    h=hex(n)
    print(h)
elif(ch==11):
    n=bin(input("Enter the binary number"))
    o=oct(n)
    print(o)
elif(ch==12):
    n=bin(input("Enter the binary number"))
    o=hex(n)
    print(o)
elif(ch==13):
    n=oct(input("Enter the octahedral number"))
    o=hex(n)
    print(o)
elif(ch==14):
    n=hex(input("Enter the hexadecimal  number"))
    o=oct(n)
    print(o)
    
else:
    print("Invalid choice")
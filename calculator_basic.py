# calculator

#lets start with input methods for the value

a= input("Please enter a value: ")
b= input("Please enter second value: ")

def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def multiply(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a/b
    print(c)
#lets make user to choose the method to be exsecute with the operator

if Method == "addition":
    add()
elif Method =="Substraction":
    sub()
elif Method =="Multiplication":
    multiply
else :
    Method =="Division"
    div()

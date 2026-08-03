def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "cannot Divide by zero"
    return a/b
def modulus(a,b):
    if b == 0:
        return "cannot Divide by zero "
    return a%b
def power(a,b):
    return a**b
while True:
    print("1.Addition")
    print("2.subtract")
    print("3.multipication")
    print("4.division")
    print("5.modulus")
    print("6.power")
    print("7.Exit")
    
    
    choice = int(input("enter a choice:"))
    if choice == 7:
        print("calculator closed")
        break
    if choice < 1 or choice > 7:
        print("Invalid input")
        continue

    num1=float(input("enter a number:"))
    num2=float(input("enter a number:"))
    
    
    if choice == 1:
        print("Result:",add(num1,num2))
    elif choice == 2:
        print("Result:",subtract(num1,num2))
    elif choice == 3:
        print("Result:",multiply(num1,num2))
    elif choice == 4:
        print("Result:",divide(num1,num2))
    elif choice == 5:
        print("Result:",modulus(num1,num2))
    elif choice == 6:
        print("Result:",power(num1,num2))
    
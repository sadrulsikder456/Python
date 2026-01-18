# Error

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Variable is not defined")


try:
    a=int(input("Enter number a:"))
    b=int(input("Enter number b:"))
    if 1>3:
        print("hello")


    print("Divition is ",a/b)
except Exception as e:
    print(e)
    print("Invalid input, please enter integers only.")
    
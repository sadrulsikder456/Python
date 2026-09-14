try:
    num1 = int(input("Enter the 1st number:"))
    num2 = int(input("Enter the 2nd number:"))
    result = num1 // num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: can't divided by zero")

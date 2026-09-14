try:
    num1 = int(input("Enter the 1st number:"))
    num2 = int(input("Enter the 2nd number:"))
    result = num1 // num2
    print(f"The result is: {result}")
except ValueError:
    print("Error: can't input except integer")
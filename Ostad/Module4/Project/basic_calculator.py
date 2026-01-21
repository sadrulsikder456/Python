# Addition Function


def addition(a, b):
    return a + b


# Subtraction Function
def substraction(a, b):
    return a - b


# Multiplication Function
def multiplication(a, b):
    return a * b


# Division Function
def division(a, b):
    if b == 0:
        return None
    return a / b

# Menu Function
def show_menu():
    print("-" * 30)
    print("Basic Calculator")
    print("=" * 40)
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)
    while True:
        try:
            choice = int(input("Enter choice:"))
            if choice in [1,2,3,4]:
                try :
                    num1 =float(input("Enter first number:"))
                    num2 =float(input("Enter second number:"))
                    if choice ==1:
                        print(f"{num1} + {num2} = {addition(num1,num2)}")
                    elif choice == 2 :
                        print(f"{num1} - {num2} = {substraction(num1,num2)}")
                    elif choice == 3:
                        print("{num1} * {num2} = {multiplication(num1,num2)}")
                        result = division(num1,num2)
                        if result is None:
                            print("Error: Division by Zero is  not allowed.")
                        else:
                            print(f"{num1} / {num2} = {result})")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
                    continue
            elif choice == 5:
                print("Exiting the calculator. Goodbye!")
                break
            # elif choice not in [1,2,3,4,5]:
            #     print("Invalid choice. Please select a number between 1 and 5.")
            #     continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
show_menu()
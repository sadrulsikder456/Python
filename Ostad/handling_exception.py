
try:
    with open("Ostad/name.txt", "r") as f:
        content = f.read()
        print(content)
    print(10/10)
    # x= int("abc")
except ZeroDivisionError:
    print("An error occurred: Division by zero is not allowed.")
except FileNotFoundError:
        print("An error occurred while reading the file:", FileNotFoundError)
except Exception as e:
    print("An unexpected error occurred:", e)
else :
    print("File read successfully and no exceptions occurred.")
finally:
    print("Execution completed.")
def check_file(filename):
    if not filename.endswith('.txt'):
        raise ValueError("Only .txt files are allowed.")
    print("File is valid.")
check_file("Ostad/name.txt")
    
         
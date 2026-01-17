# without parameter and return value
def say_hello():
    print("Hello")


# with parameter and without return value
def sum(a, b):
    print(a + b)


# with parameter and with return value
def mul(a, b):
    return a * b


# without parameter and with return value
def get_pie():
    return 3.14


say_hello()

sum(5, 6)
result = mul(4, 5)
print("Multiplication:", result)
pie = get_pie()
print("Value of pie:", pie)

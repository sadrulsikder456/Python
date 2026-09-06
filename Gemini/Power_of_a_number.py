def power(x,y):
    if y==0:
        return 1
    return power(x,y-1)*x

x=int(input("Enter the base number:"))
y=int(input("Enter the power:"))
result=power(x,y)
print(f"the result of {x} raised to the power of {y} is: {result}")
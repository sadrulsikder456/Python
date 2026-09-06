def febonacci(number):
    if number==0:
        return 0
    elif number==1:
        return 1
    return febonacci(number-1)+febonacci(number-2)

number=int(input("Enter a number:"))
result=febonacci(number)
print(f"The {number}th Fibonacci number is: {result}")
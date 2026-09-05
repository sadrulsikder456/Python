def sum(number):
    if number==1:
        return 1
    return sum(number-1)+number

num=int(input("Enter a number:"))
print("The sum of first",num,"numbers is:",sum(num))
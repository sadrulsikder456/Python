# TODO: Aita holo funtion ar bitore abr function ccall kore recursion use kore factorial ber kora. Ekhane amra function ar bitore function call kore recursion use kore factorial ber korbo.
def get_factorial(number):
    if number==0:
        return 1
    return get_factorial(number-1)*number
number=int(input("Enter a number:"))
factorial_number=get_factorial(number)
print(f"The factorial of {number} is : {factorial_number}")


 #TODO: Aita holo akta function ar bitore just normaly loop caliye factorial ber kora. Ekhane amra function ar bitore loop caliye factorial ber korbo.
def getfactorial_of_a_number(number):
    factorial_sum=1
    for i in range(1,number+1):
        factorial_sum*=i
    return factorial_sum

number=int(input("Enter a number:"))
factorial_of_a_number=getfactorial_of_a_number(number)
print(f"The factorial of {number} is : {factorial_of_a_number}")
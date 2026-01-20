x=10 #Global variable

print(x)
def func():
    y=19 #Local variable
    x=100
    print(x)
    print(y)
func()

n="Global" #Global variable
def outer():
    
    n="Enclosing" #Enclosing variable
    def inner():
        global n
        n="Local" #Local variable
        print(n)
    inner()
    print(n)
outer()
print(n)
def my_func(f_name,l_name,age):
    print(f"My name is {f_name} {l_name} and i am {age} years old")

my_func(age=25,l_name ="Amin" ,f_name="Sadrul")

def my_func1(**kwargs):
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']} and i am {kwargs['age']} years old")

my_func1(age=25,l_name ="Amin" ,f_name="Sadrul")
class person:
    def __init__ (self,age):
        self._age=age
    
    def set_age(self,age):
        if age<0:
            print("Age cannot be valid, setting age to 0")
        else:
            self._age=age
    def get_age(self,age):
        if age<0:
            print("Age is not valid, setting age to 0")
        elif (age>0 and age <13):
            print("You are young.")
        elif(age>=13 and age<18):
            print("you are teenager.")
        else:
            print("Your are old.")

t = int(input())

for i in range(t):
    age= int(input())
    p=person(age)
    p.get_age(age)
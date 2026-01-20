class BankAccount:
    def withdraw(self,amount):
        print(f"Withdrawing {amount} from the account")
# Inheritance

class savings_account(BankAccount):
    pass

class Student_account(BankAccount):
    pass
s_acc = savings_account()
s_acc.withdraw(5000)


class Camera:
    def take_photo(self):
        print("Taking Photo")
class GPS:
    def get_location(self):
        print("Getting Location")

class SmartPhone(Camera,GPS):
    pass
sp=SmartPhone()
sp.take_photo()
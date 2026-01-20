# Constructor

class BankAcount:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def get_info(self):
        print(f"Accoint Holder Name: {self.account_holder}, and The Balance is :{self.balance}")

acc1 = BankAcount("Sadrul", 2700)
acc1.get_info()
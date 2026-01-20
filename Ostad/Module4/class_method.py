# Constructor

class BankAcount:
    bankname="Dutch Bangla Bank"
    @classmethod
    def chance_bank_name(cls,new_name):
        cls.bankname=new_name
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def get_info(self):
        print(f"Accoint Holder Name: {self.account_holder}, and The Balance is :{self.balance}")

acc1 = BankAcount("Sadrul", 2700)
acc1.get_info()

print(BankAcount.bankname)

# Changing bank name using class method
BankAcount.chance_bank_name("Islami Bank ")
print(BankAcount.bankname)
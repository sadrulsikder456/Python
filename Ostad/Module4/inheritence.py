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
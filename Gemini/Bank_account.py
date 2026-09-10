class BankAccount:
    def __init__(self,account_holder,balance):
        self.name=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f" The deposited amount is :{amount} & the new balance is {self.balance}")
    def withdraw(self,amount):
        if amount> self.balance:
            print("Insufficiant balance")
        else:
            self.balance-=amount
            print(f"The withdraw balance is : {amount} & the new balance is {self.balance}")

my_account=BankAccount("Sadrul", 1000)
my_account.deposit(500)
my_account.withdraw(1000)
my_account.withdraw(5000)
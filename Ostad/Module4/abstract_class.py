from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def withdraw(self):
        print("This is an abstract method for withdrawing money")


class savings_account(BankAccount):
    def withdraw(self):
        print("Withdrawing money from Savings Account")


s_acc = savings_account()
s_acc.withdraw()

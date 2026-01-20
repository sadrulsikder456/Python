class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number 
        self._balance = balance 
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        self._balance = amount

ba=BankAccount("123456789", 5000)
print(ba.balance)
ba.balance=90900
print(ba.balance)
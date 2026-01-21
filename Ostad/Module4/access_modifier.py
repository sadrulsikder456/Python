class BankAccount:
    def __init__(self,o):
        self.owner=0                #public
        self._balance=0             #protected
        self.__address="Dhaka"      #private
    
ba =BankAccount("Sadrul")
print(ba._balance)
print(ba._BankAccount__address)
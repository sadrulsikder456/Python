class BankAccount:
    @staticmethod
    def validate_account_number(account_number):
        if account_number%2==0:
            return "Valid Account Number"
        else:
            return "Invalid Account Number"
    
re= BankAccount.validate_account_number(123456)
print(re)
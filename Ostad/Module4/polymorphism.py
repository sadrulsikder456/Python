class payment:
    def process_payment(self):
        print("Processing payment in a generic way")

class PaymentToBank:
    def process_payment(self):
        print("Processing payment to Bank Account")

class CreditCardPayment(payment,PaymentToBank):
    def process_payment(self):
        print("Processing payment through Credit Card")
        super().process_payment()

class PayPalPayment(payment):
    def process_payment(self):
        print("Processing payment through PayPal")

p=payment()
p.process_payment()
ccp=CreditCardPayment()
ccp.process_payment()



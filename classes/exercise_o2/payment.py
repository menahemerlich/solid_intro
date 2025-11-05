
class Payment:
    def pay(self, amount):
        print(f"amount: {amount}")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"amount: {amount}")

class PayPalPayment:
    def pay(self, amount):
        print(f"amount: {amount}")

class CryptoPayment:
    def pay(self, amount):
        print(f"amount: {amount}")



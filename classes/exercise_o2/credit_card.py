from classes.exercise_o2.payment import Payment

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"amount: {amount}")
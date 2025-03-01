# Payment Method Program using Polymorphism
class Payment:
    def pay(self, amount):
        print(f"Payment mode: ${amount}")
class Cash(Payment):
    def __init__(self, cash):
        self.cash = cash

    def pay(self, amount):
        print(f"Cash payment of ${amount}")
class Card(Payment):
    def __init__(self, card):
        self.card = card

    def pay(self, amount):
        print(f"Card payment of ${amount} using card ending in {self.card}.")
class Cheque(Payment):
    def __init__(self, cheque):
        self.cheque = cheque

    def pay(self, amount):
        print(f"Cheque payment of ${amount} with cheque number {self.cheque}.")

if __name__ == "__main__":
    payment_methods = {
        "1": Cash("Cash"),
        "2": Card("12345678901"),
        "3": Cheque("987654")
    }

    print("Select payment method:")
    print("1. Cash")
    print("2. Card")
    print("3. Cheque")

    choice = input("Enter your choice (1/2/3): ")
    amount = float(input("Enter amount to pay: "))

    if choice in payment_methods:
        payment_methods[choice].pay(amount)
    else:
        print("Invalid choice!")

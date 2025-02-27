# Bank Account Management System with Inheritance

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New Balance: ${self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New Balance: ${self.balance}"
        return "Insufficient balance or invalid amount!"

    def get_balance(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)


acc1 = BankAccount("Dua", 1000)
acc2 = SavingsAccount("Fatima", 5000)

acc1.balance += 200 
print(f"Manual Update: New balance of {acc1.account_holder} is ${acc1.balance}")

print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.get_balance())
print(acc2.get_balance())


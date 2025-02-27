# Bank Account Management System with Encapsulation and Inheritance

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New Balance: ${self.__balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New Balance: ${self.__balance}"
        return "Insufficient balance or invalid amount!"

    def get_balance(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.__balance}"

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            return f"Balance updated. New Balance: ${self.__balance}"
        return "Balance cannot be negative!"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)
acc1 = BankAccount("Dua", 1000)
acc2 = SavingsAccount("Fatima", 5000)
print(acc1.set_balance(int(acc1.get_balance().split("$")[-1])))  
print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.get_balance())
print(acc2.get_balance())
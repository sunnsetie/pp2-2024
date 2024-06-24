class Account:
    def __init__(self, owner, balance=0): 
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount): 
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

owner = input()
x = int(input())
y = int(input())
z = int(input())
balance = float(input())
acc= Account(owner, balance)

acc.deposit(x)
acc.withdraw(y)
acc.withdraw(z)
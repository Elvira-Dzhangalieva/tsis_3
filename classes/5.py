class Account():
    def __init__(self, owner = " ", balance = 0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"owner:{self.owner}\nbalance:{self.balance}"
    
    def deposit(self, amount):
        self.balance +=amount
        print("Deposit Accepted")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawl accepted:")
        print("Funds Unavailable!")


acnt = Account('Aizada', 100)
print(acnt)

acnt.deposit(52)

acnt.withdraw(75)

acnt.withdraw(500)
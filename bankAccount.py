class BankAccount:
    Accounts = []
    def __init__(self,int_rate,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.Accounts.append(self)
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    def yield_interest(self):
        if self.balance >0:
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def printAccounts(cls):
        print(f"\nThere are {len(cls.Accounts)} bank accounts:")
        for i in cls.Accounts:
            print(f"\nAccount #{cls.Accounts.index(i)+1}")
            i.display_account_info()

ac1 = BankAccount(0.1,15)
ac1.deposit(10).deposit(15).deposit(25).withdraw(20).yield_interest().display_account_info()
ac2=BankAccount(0.2,5)
ac2.deposit(10).deposit(50).withdraw(1).withdraw(2).withdraw(8).withdraw(100).yield_interest().display_account_info()
BankAccount.printAccounts()
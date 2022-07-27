class BankAccount:
    Intrest_rate = 0.01
    Balance = 0
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        balance = (balance) + (amount)
    def withdraw(self, amount):
        balance = (balance) - (amount)
    def display_account_info(self):
        print(BankAccount.intrest_rate)
        print(BankAccount.balance)
    def yield_interest(self):
        print((BankAccount.balance) * (BankAccount.intrest_rate))


Adam = BankAccount(0.03, 3756)
Theo = BankAccount(0.04, 874)

Adam.deposit(25)
Adam.deposit(17)
Adam.deposit(183)
Adam.withdraw(450)
Adam.yield_interest()
Adam.display_account_info()
print()
Theo.deposit(25)
Theo.deposit(17)
Theo.withdraw(183)
Theo.withdraw(450)
Theo.withdraw(25)
Theo.withdraw(100)
Theo.yield_interest()
Theo.display_account_info()
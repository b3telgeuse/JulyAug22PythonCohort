class User:
    def __init__(self, name="John Doe", starting_balance=0, interest_rate=0.03):
        self.name = name
        self.account = BankAccount(starting_balance, interest_rate)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self



class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, balance=0, interest=0.3):
        self.balance = balance
        self.interest_rate = interest
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds.")
        else:
            print("Withdrawing $" + str(amount)) 
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Account Balance: $" + str(self.balance))
        print("Interest Rate:", self.interest_rate)
        return self

    def yield_interest(self):
        print("Yielding interest...")
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum

    @classmethod
    def print_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        return cls



Adam = User("Adam Ulrich")
Adam.display_user_balance().make_deposit(100).display_user_balance()
print()
Adam.display_user_balance().make_withdrawal(55)
Adam.yield_interest().display_user_balance()
print()
print()
Theo = User(name="Theo Oakley", interest_rate=0.02)
Theo.display_user_balance().make_deposit(500)
print()
Theo.display_user_balance().make_withdrawal(150)
Theo.yield_interest().display_user_balance()
print()


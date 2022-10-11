class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5

        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self


account_1 = BankAccount(.10, 300)
account_2 = BankAccount(.10, 500)

account_1.deposit(5).deposit(10).deposit(15).withdraw(20).yield_interest().display_account_info()
account_2.deposit(205).deposit(300).withdraw(20).withdraw(15).withdraw(10).withdraw(5).yield_interest().display_account_info()


class BankAccount: # creating a class and calling it BankAccount
    # indent 4 lines to include method to class
    
    def __init__(self, int_rate, balance): # method w/ constructor: __intit__ with parameters (self, init_rate, balance)
        self.int_rate = int_rate 
        self.balance = balance
        
    def deposite(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount 
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -5
        return self
    
    def display_account_info(self):
        print("Balance: ", f"{self.balance}")

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    def make_deposit(self, amount):
        self.account.deposite(amount)
        return self

    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
    
    def yeild_interest_(self):
        self.account.yeild_interest()
        return self

user1 = User("Bernard", "B@b.com")

user1.display_user_balance()
user1.make_deposit(1000).display_user_balance()
user1.make_withdrawl(500).display_user_balance()
user1.yeild_interest_().display_user_balance()













# user1 = BankAccount(.04, 1000)
# user1.display_account_info()

# user1.deposite(500).display_account_info()
# user1.withdraw(250).display_account_info()
# user1.yeild_interest().display_account_info()
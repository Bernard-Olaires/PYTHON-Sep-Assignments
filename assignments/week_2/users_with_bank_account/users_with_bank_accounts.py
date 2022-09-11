
class User:
    def __init__(self, name="Unassigned"):
        self.name = name
        self.accounts = {}

    def open_new_account(self, with_amount=0, interest=0.04, account_type="checking"):
        print("Creating new account", [account_type])
        self.accounts[account_type] = BankAccount(with_amount, interest, account_type)
        
    # creating a method(function) that decreases the users balance by specified amount
    
    def make_withdraw(self, amount, account_type="checking"):
            self.accounts[account_type].withdraw(amount)
            return self

    #creating a method that prints name and account balance
    def display_user_balance(self):
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        return self

    def make_deposit(self, amount, account_type="checking"):
        self.accounts[account_type].deposit(amount)
        return self
    
    def yeild_interest(self):
        print("Yieling Interest")
        self.balance += (self.balance * self.interest_rate)
        return self

class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    
    def __init__(self, balance= 0, interest =.04, account_type = "checking"):
        self.balance = balance
        self.interest_rate = interest 
        self.account_type = account_type
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        print("Depositing $" + str(amount))
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("insufficient Funds: Charging a $5 fee")
        else:
            print("Withdrawing $" + str(amount))
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Account Balance: $" + str(self.balance))
        print("Interest Rate:", self.interest_rate)
        return self 
    
    def yeild_interest(self):
        print("Yieling Interest")
        self.balance += (self.balance * self.interest_rate)
        return self
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()


user1 = User("Bernard")
user1.open_new_account(with_amount=100, interest=0.04)
user1.display_user_balance()

print("------------------------------------") #divide each display for output
user1.make_deposit(100).display_user_balance()

print("------------------------------------") #divide each display for output

user1.make_withdraw(50).display_user_balance()
print("------------------------------------") #divide each display for output
user1.yeild_interest().DISPL()

from re import A


class User:
    
    def __init__(self, name="Unassigned"):
        self.name = name
        self.accounts = {}

    def open_new_account(self, with_amount=0, interest=0.04, account_type="checking"):
        print("Creating new account..")
        self.accounts[account_type] = BankAccount(with_amount, interest, account_type)
        
    # creating a method(function) that decreases the users balance by specified amount
    def make_withdraw(self, amount, account_type="checking"):
            self.accounts[account_type].withdraw(amount)
            return self

    #creating a method that prints name and account balance
    def display_user_balance(self):
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def yeild_interest(self):
        self.account.yeild_interest()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ", {self.balance})
    
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            BankAccount.display_account_info()


bernard = User("Bernard Olaires")

bernard.display_user_balance().make_deposit(100).withdrawl(50).display_user_balance()

b





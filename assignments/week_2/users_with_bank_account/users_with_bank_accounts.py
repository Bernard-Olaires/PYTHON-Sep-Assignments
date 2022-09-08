class User:
    
    def __init__(self, name="Unassigned", starting_balance=0, interst_rate=0.04):
        self.name = name
        self.account = BankAccount(starting_balance, interst_rate)
        
    def withdrawl(self, amount):
            self.account.withdraw(amount)
            return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
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
            account.display_account_info()


bernard = User("Bernard Olaires")

bernard.display_user_balance().make_deposit(100)

bernard.make_deposit()



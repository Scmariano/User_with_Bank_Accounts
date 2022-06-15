
class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else :
            print("Insufficient funds: Charging a $5 fee ")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
    



class User:
# Update the User class __init__ method
    def __init__ (self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name
        self.savings = BankAccount(0.04,500)
        self.checking = BankAccount(0.3, 1000)
        
# Add a display_user_balance method to the User class that displays user's account balance
    def display_info(self):
        print()
# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
        print(f"User : {self.firstName} {self.lastName}, Savings Balance: {self.savings.balance}")
        print(f"User : {self.firstName} {self.lastName}, Checking Balance: {self.checking.balance}")
        return self

# Add a make_deposit method to the User class that calls on it's bank account's instance methods.
    def make_deposit(self):
        self.savings.deposit(500)
        self.checking.deposit(100)
        return self
# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
    def make_withdrawal(self):
        self.savings.withdraw(180)
        self.checking.withdraw(150)
        return self
# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.
    def transfer(self, amount, name):
        self.balance = self.balance - amount
        name.balance = name.balance + amount 
        self.display_info()
        name.display_info()
        return self
    
        

User_Stephen = User("Stephen", "Mariano")
User_Stephen.make_deposit().make_withdrawal().display_info()




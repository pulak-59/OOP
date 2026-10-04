class account:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
            print(f"Tk {amount} is added succesfully")

    def get_balance (self):
        return self.balance

bnkacc = account("pulak", 5000)
bnkacc.deposit(2000)
bnkacc.get_balance()
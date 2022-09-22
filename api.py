import math

class User:
    def __init__(self, name = "") -> None:
        self.name = name
        self.balance = 0
        self.owed = {}
    
    def show(self, verbose=True):
        for owed_user, owed_balance in self.owed.items():
            if owed_balance > 0:
                print(f"{self.name} owes {owed_user}: {owed_balance}")
            elif verbose and (owed_balance < 0):
                print(f"{owed_user} owes {self.name}: {-owed_balance}")
    
    def owe(self, payer, owed_balance):
        # Reduce balance
        self.balance -= owed_balance
        # Increase self -> payer
        if payer in self.owed:
            self.owed[payer] += owed_balance
        else:
            self.owed[payer] = owed_balance
        # Decrease payer -> self
        if self.name in users[payer].owed:
            users[payer].owed[self.name] -= owed_balance
        else:
            users[payer].owed[self.name] = -owed_balance

users = {}

def show(user_list):

    verbose = True
    if len(user_list) == 0:
        user_list = list(users.keys())
        verbose = False
    
    is_no_balance = True
    for user in user_list:
        if user in users:
            if users[user].balance != 0:
                is_no_balance = False
                users[user].show(verbose)
        else:
            print(f"Unknown user '{user}'")
    
    if is_no_balance:
        print("No balances")

def expense_equal(payer, balance, payees):
    # Check payer existance
    if payer not in users:
        print(f"Unknown payer '{payer}'")
        return
    # Increase payer balance
    users[payer].balance += balance
    # Iterate through payee
    for index, payee in enumerate(payees):
        # Check payee existance
        if payee not in users:
            print(f"Unknown payee '{payee}'")
            return
        # Calculate owed balance
        owed_balance = balance / len(payees)
        if index == 0:
            owed_balance = math.ceil(owed_balance * 100) / 100
        else:
            owed_balance = math.floor(owed_balance * 100) / 100
        # Perform owe
        users[payee].owe(payer, owed_balance)

def expense_exact(payer, balance, payees, exacts):
    # Check payer existance
    if payer not in users:
        print(f"Unknown payer '{payer}'")
        return
    # Check sum equal to balance
    if sum(exacts) != balance:
        print(f"Total values ({sum(exacts)}) not equal to balance ({balance})")
        return
    # Increase payer balance
    users[payer].balance += balance
    # Iterate through payee
    for payee, owed_balance in zip(payees, exacts):
        # Check payee existance
        if payee not in users:
            print(f"Unknown payee '{payee}'")
            return
        # Perform owe
        users[payee].owe(payer, owed_balance)

def expense_percent(payer, balance, payees, percents):
    # Check payer existance
    if payer not in users:
        print(f"Unknown payer '{payer}'")
        return
    # Check sum equal to balance
    if sum(percents) != 100.0:
        print(f"Total percentage ({sum(percents)}) not equal to 100.0")
        return
    # Increase payer balance
    users[payer].balance += balance
    # Iterate through payee
    for payee, percent in zip(payees, percents):
        # Check payee existance
        if payee not in users:
            print(f"Unknown payee '{payee}'")
            return
        # Perform owe
        users[payee].owe(payer, balance * (percent / 100.0))
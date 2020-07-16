
class InsufficientBalance(Exception):
    pass

class Account(object):
    ''' Simple class with money account'''

    def __init__(self, initial_amount = 0, name = "", cust_id=0):
        self.balance = initial_amount
        self.name = name
        self.id = cust_id

    def display(self):
        print("Account is under {} with id {} and current balance is {}" .format(self.name, self.id, self.balance))

    def credit(self, amount=0):
        self.balance += amount

    def debit(self, amount):
        if (self.balance - amount < 0):
            raise(InsufficientBalance("Not enough balance in account. Balance is {}" .format(self.balance)))
        self.balance -= amount

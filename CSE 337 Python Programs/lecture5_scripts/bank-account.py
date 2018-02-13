class BankAccount(object):
   # define a class to simulate a bank account
   def __init__ (self):
      # initialize the bank account with zero balance
      self.balance = 0
   def __init__(self, balance = 0):
      self.balance = balance
   def deposit (self, amount):
      # deposit the given amount into the account
      self.balance = self.balance + amount
   def withdraw (self, amount):
      # withdraw the given amount from the account
      self.balance = self.balance - amount
   def get_balance (self):
      # return the balance in the account
      return self.balance
   def transfer(self, amount, toAccount):
      # transfer the amount from one account to another
      self.withdraw(amount)
      toAccount.deposit(amount)

my_account = BankAccount()
second_account = BankAccount()

my_account.deposit(200)
second_account.deposit(125)
my_account.withdraw(75)
second_account.withdraw(50)

print my_account.get_balance()
print second_account.get_balance()


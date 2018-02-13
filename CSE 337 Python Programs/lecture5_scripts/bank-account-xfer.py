class BankAccount(object):
   # define a class to simulate a bank account
   def __init__ (self, initamount):
      # initialize the bank account with zero balance
      self.balance = initamount 
   def deposit (self, amount):
      # deposit the given amount into the account
      self.balance = self.balance + amount
   def withdraw (self, amount):
      # withdraw the given amount from the account
      self.balance = self.balance - amount
   def getBalance (self):
      # return the balance in the account
      return self.balance

   def transfer (self, amount, toAccount):
      # transfer the amount from one account to another
      self.withdraw(amount)
      toAccount.deposit(amount)

myAccount = BankAccount(500)
newAccount = BankAccount(100)

myAccount.transfer(200, newAccount)

print myAccount.getBalance()
print newAccount.getBalance()


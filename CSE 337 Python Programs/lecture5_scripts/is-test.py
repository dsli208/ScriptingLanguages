class BankAccount(object):
   # define a class to simulate a bank account
   def __init__ (self, init_bal):
      self.balance = init_bal

   def deposit (self, amount):
      # deposit the given amount into the account
      self.balance = self.balance + amount
   def withdraw (self, amount):
      # withdraw the given amount from the account
      self.balance = self.balance - amount
   def get_balance (self):
      # return the balance in the account
      return self.balance

class CheckingAccount (BankAccount):
   def __init__ (self, init_bal):
      BankAccount.__init__ (self, init_bal)
      self.checkRecord = {}

   def process_check (self, number, to_who, amount):
      self.withdraw(amount)
      self.check_record[number] = (to_who, amount)

   def check_info (self, number):
      if self.check_record.has_key(number):
         return self.check_record[number]
      else:
         return 'no such check'

my_account = BankAccount(0)
second_account = BankAccount(0)
ca = CheckingAccount(300)

print type(my_account)
print type(BankAccount)
print type(CheckingAccount)

print isinstance(my_account, CheckingAccount)
print isinstance(my_account, BankAccount)
print isinstance(ca, CheckingAccount)
print isinstance(ca, BankAccount)

print issubclass(CheckingAccount, BankAccount)


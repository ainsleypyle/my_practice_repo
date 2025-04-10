from bank_account import BankAccount

account1=BankAccount("1234", 1000)
print(account1)
account1.deposit(1000)
print(account1)

account2=BankAccount("4567", 5)
print(account2)
account2.deposit(5)
print(account2)

account1.withdraw(1000)
print(account1)
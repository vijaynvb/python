class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance   

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ₹{amount}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Avinash", 10000)

account.deposit(2000)
account.withdraw(1500)

print("Current Balance:", account.get_balance())

 
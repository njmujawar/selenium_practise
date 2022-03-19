from abc import ABC, abstractmethod


class Bank(ABC):        # abstract class

    def __init__(self):
        self.bal = 20000

    @abstractmethod
    def balance(self):
        print("the balance is:", self.bal)

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
       pass

# b = Bank()  # TypeError: Can't instantiate abstract class Bank with abstract methods balance, deposit, withdraw


class SBI(Bank):

    def balance(self):
        print("the balance is:", self.bal)

    def withdraw(self, amount):
        self.bal -= amount
        self.balance()

    def deposit(self, amount):
        self.bal += amount
        self.balance()


sbi = SBI()
sbi.withdraw(3000)
sbi.deposit(5000)















class BankAccount:
    __roi = 4.5

    def display(self):
        print("roi in BankAccount:", self.__roi)


class SavingsAccount(BankAccount):
    __roi = 2.5

    def print_(self):
        print("roi in SavingsAccount:", self.__roi)


# s = SavingsAccount()
# s.print_()
##################################################################

















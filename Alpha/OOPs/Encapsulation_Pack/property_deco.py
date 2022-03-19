class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, new_value):
        self.__marks = new_value

    @marks.deleter
    def marks(self):
        del self.__marks


class Account:

    def __init__(self, bank, bal, acc_no):
        self.bank = bank
        self.__bal = bal
        self.__acc = acc_no

    @property
    def balance(self):
        return self.__bal

    @balance.setter
    def balance(self, new_value):
        raise TypeError("Balance cannot be changed")

    @property
    def account(self):
        return self.__acc

    @account.setter
    def account(self, new_value):
        raise TypeError("Account numbr cannot be modified")


# a = Account("Canara", 10000, 12345678)
# # print(a.balance)
# # a.balance = 20000
# print(a.account)
# a.account = 23342


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        # print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')

p = Person('Adam')
print(p.name.__doc__)
print(p.name)
p.name = 'John'
del p.name








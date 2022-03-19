#### public members

class Public:
    name = "Ram"

    def display(self):
        print("in public display",self.name)


# accessing outside the class
# p = Public()
# print(p.name)
# p.display()


# accessing in child class
class Child(Public):
    def spam(self):
        print(self.name)
        self.display()

# c  = Child()
# print(c.name)
# print(c.display())

""" Protected members """

class Protected:
    _name = "Sita"

    def _display(self):
        print("name is: ", self._name)


# accessing outside the class
p = Protected()
# print(p.name)       # AttributeError
# print(p._name)
# p._display()

# accessing in child class
class Child(Protected):
    def spam(self):
        print(self._name)
        self._display()


# c = Child()
# c.spam()
##########################################################

class Private:
    __name = "Steve"

    def __display(self):
        print("in Private class display:", self.__name)


# accessing outside the class
p = Private()
print(p.name)       # AttributeError
print(p.__name)       # AttributeError
print(Private.__dict__)
# {'_Private__name': 'Steve', '_Private__display': <function Private.__display at 0x00}
print(p._Private__name)

# accessing in child class

class Child(Private):

    def spam(self):
        print(self.__name)      # AttributeError


c = Child()
c.spam()



































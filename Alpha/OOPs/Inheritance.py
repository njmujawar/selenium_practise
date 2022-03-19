# class Parent:
#     name = "Ram"
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass

#
# p = Parent(1, 2)
# c = Child1(12, 45)
# print(c.name)

class Parent1:
    a = 10
    def display(self):
        print("in parent1 display")

class Parent2:
    b = 25
    def display(self):
        print("in parent2 display")

class Child(Parent1, Parent2):
    a = 80

    def display(self):
        print("in Child display")
        super().display()
        Parent2.display(self)

# c = Child()
# c.display()


class Sample:
    """ This class is built for displaying some message"""

    def __init__(self):
        pass

    def display(self):
        pass


# printing documentation string
# print(Sample.__doc__)










































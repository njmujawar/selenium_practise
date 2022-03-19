# without classmethod
class ChiefMinister:
    current_CM = "Yediyurappa"

    def display(self):
        print(self.current_CM)

    def replacement(self, votes):
        if votes > 50:
            self.current_CM = "Bommai"


# bjp = ChiefMinister()
# bjp.replacement(51)
# bjp.display()                   # Bommai
# com_people = ChiefMinister()
# com_people.display()            # Yediyurappa
# opposition = ChiefMinister()
# opposition.display()            # Yediyurappa

# using classmethod
class ChiefMinister:
    current_CM = "Yediyurappa"

    def display(self):
        print(self.current_CM)

    @classmethod
    def replacement(cls, votes):
        if votes > 50:
            cls.current_CM = "Bommai"


# bjp = ChiefMinister()
# bjp.replacement(51)
# bjp.display()                   # Bommai
# com_people = ChiefMinister()
# com_people.display()            # Bommai
# opposition = ChiefMinister()
# opposition.display()            # Bommai


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.sal = salary

    def display(self):
        print(self.name, self.sal)

    @classmethod
    def spam(cls):
        e1 = cls("shyam", 10000)
        e1.display()


# e = Employee("Ram", 20000)
# e.spam()        # "shyam", 10000
class Employee:

    def __init__(self):
        self.a = 10

    def __call__(self):
        print("in call method")

e = Employee()
print(callable(Employee))
print(callable(e))
e()



























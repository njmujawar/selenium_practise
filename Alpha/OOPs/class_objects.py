class Employee:
    fname = "steve"     # class variables
    lname = "jobs"      # class variables


# creating an object/instance
emp = Employee()

# accessing class variables using objects
print(emp.fname)
print(emp.lname)

# accessing class variables using class
print(Employee.fname)
print(Employee.lname)

# __dict__ --> returns
print(dir(Employee))
print(Employee.__dict__)
print(dir(emp))
print(emp.__dict__)

######################################################################
def display(self, fname, lname):
    print("The name of the employee is", fname, lname)
    print(self.fname, self.lname)


# creating Constructor in a class
class Employee:
    fname = "steve"     # class variables
    lname = "jobs"      # class variables

    # constructing an object with object variables
    def __init__(self, first, last):
        self.a = first      # object variables
        self.b = last       # object variables


# creating an object/instance
emp1 = Employee("Tata", "Birla")
emp2 = Employee("Mukhesh", "Ambani")

# object attributes/variables
print(emp1.__dict__)        # {'a': 'Tata', 'b': 'Birla'}
print(emp2.__dict__)        # {'a': 'Mukhesh', 'b': 'Ambani'}

# accessing object attibutes using object
print(emp1.a)   # Tata
print(emp2.b)   # Ambani

# accessing object attibutes using object
print(Employee.a)   # Attribute Error


############################################################################
# creating object variables with the same name as class variables

class Employee:
    fname = "steve"     # class variables
    lname = "jobs"      # class variables

    # constructing an object with object variables
    def __init__(self, first, last):
        self.fname = first      # object variables
        self.lname = last       # object variables


# creating an object/instance
emp1 = Employee("Tata", "Birla")
emp2 = Employee("Mukhesh", "Ambani")

print(emp1.__dict__)    # {'fname': 'Tata', 'lname': 'Birla'}
print(Employee.__dict__)    # {'fname': 'steve', 'lname': 'jobs'}
print(emp1.fname)       # Tata
print(Employee.fname)   # steve


################################################################
# modification w.r.t class variables

class Numbers:
    a = 10
    b = 20

    def __init__(self, c, d):
        self.a = c
        self.d = d

    def display(self):
        print("the numbers in class variables are: ", Numbers.a, Numbers.b)
        print("the numbers in object variables are: ", self.a, self.b, self.d)


n = Numbers(30, 40)
print(n)
print(Numbers)
Numbers.display(n)


####################################################################
class Student:

    def __init__(self, s_name, s_id, dob):
        self.s_name = s_name
        self.s_id = s_id
        self.dob = dob

    def validate(self):
        date, month, year = self.dob.split("/")
        if abs(int(year) - 2021) > 18:
            print(f"{self.s_name} is over 18 years of age")
        else:
            print(f"{self.s_name} is not over 18 years of age")


s1 = Student("Ram", 1, "01/01/1999")
s1.validate()


##############################################################
class BankAccount:

    owner = "Nikhil"
    balance = 0.0

    def deposit(self, amount):
        print("deposited amount:", amount)
        if amount > 0:
            self.balance += amount
            print("The updated balance is :", self.balance)

        else:
            print("Enter valid amount")

    def withdraw(self, amount):
        print("withdrawn amount is:", amount)

        if 0 < amount <= self.balance:
            self.balance -= amount
            print("The updated balance is :", self.balance)

        else:
            print("Enter valid amount")

    def check_balance(self):
        print("The current balance is:", self.balance)


b = BankAccount()
b.deposit(10000)
b.withdraw(1000)
b.check_balance()

#######################################################################

class ListData:

    list_ = ["hai", 12, 8.4, 98, 61]

    def add_data(self, ele):
        self.list_.append(ele)
        print(self.list_)

    def delete_data(self, ele):
        if ele in self.list_:
            self.list_.remove(ele)
        else:
            print("No such element")

    def find_length(self):
        print(len(self.list_))

    def find_data(self, ele):
        if ele in self.list_:
            print(self.list_.index(ele))

        else:
            print("element is not present")

###############################################################################

class Books:
    book_data = {}

    def add_new_book(self, *books):
        for book in books:
            d1 = {}
            d1["book_id"] = int(input("enter book id: "))
            d1["author"] = input("enter author name: ")
            d1["published_year"] = int(input("enter the year of publication: "))
            d1["price"] = float(input("enter the price: "))

            self.book_data[book] = d1
        print(self.book_data)

    def delete_book(self, book):
        print(self.book_data.pop(book, "book is not present"))

    def display_book(self, book):
        if book in self.book_data:
            print(self.book_data[book])
        else:
            print("Book is not present")

    def inquire_book(self, book):
        if book in self.book_data:
            print(f"{book} is in the stock")

        else:
            print(f"{book} is out of stock")


b = Books()
b.add_new_book("Harry Potter", "The Alchemist")
b.delete_book("book")



























































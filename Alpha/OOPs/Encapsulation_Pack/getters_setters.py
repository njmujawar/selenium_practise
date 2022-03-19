class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):        # getter
        return self.__marks

    def set_marks(self, new_value):  # setter
        self.__marks = new_value

    def delete_marks(self):     # deleter
        del self.__marks

    marks = property(get_marks, set_marks, delete_marks)

s = Student("Tom", 60)
print(s.marks)
s.marks = 78
print(s.marks)
del s.marks
print(s.marks)


"""
s.display()
print(s.__dict__)       # {'name': 'Tom', '_Student__marks': 60}
s.marks = 35
print(s.__dict__)       # {'name': 'Tom', '_Student__marks': 60, 'marks': 35}
s.display()
"""


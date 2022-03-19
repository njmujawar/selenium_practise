n = 11
# l = []
#
# for i in range(2, n):
#     if n % i != 0:
#         l.append(True)
#     else:
#         l.append(False)


# for i in range(2, n):
#     l.append(n % i != 0)
# print(l)
# print(all(l))
# print(any(l))

res = [True if n % i != 0 else False for i in range(2, n)]

def prime_():
    for num in range(1, 10):
        if num > 1 and all([num % i != 0 for i in range(2, num)]):
            yield num ** 2



# print(list(prime_()))


gen_ex = (num ** 2 for num in range(1, 10) if num > 1 and all([num % i != 0 for i in range(2, num)]))

# print(list(gen_ex))


def reverse_(func):
    def wrapper(*args, **kwargs):

        res = func(*args, **kwargs)
        return res[::-1]

    return wrapper


@reverse_   # return_string = reverse_(return_string)
def return_string(string):
    return string


# print(return_string("hello"))

def type_check(*types):   # (int, str)
    def validate(func):
        def wrapper(*args, **kwargs):

            for value, type_ in zip(args, types):   # (1, 2)
                # [(1, int), (2, str)]
                if isinstance(value, type_):
                    print(f"{value} is of type {type_}")
                else:
                    print(f"{value} is not of type {type_}")

            func(*args, **kwargs)

        return wrapper
    return validate


@type_check(int, str)
def add(a, b):
    return a + b


add(1, 2)

"""

# accessing object attibutes using object
print(emp1.a)   # Tata
print(emp2.b)   # Ambani

# accessing object attibutes using class
print(Employee.a)   # Attribute Error

"""


class A:
    l = []

    def append_(self):
        self.l.append(1)


a = A()
a.append_()
print(A.l)































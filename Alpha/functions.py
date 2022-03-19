s = "hello"
l = [1, 2, 3]


def iterable_length(iterable):  # parameters or formal arguments
    count_ = 0

    for i in iterable:
        count_ += 1

    return 1, 2, 3


res = iterable_length(s)  # arguments or actual argument

# print(res)

#
# def greet(name, age):
#     print(f"hai {name}, your age is {age}")

# # positional arguments
# greet("John", 60)
#
# # keyword arguments
# greet(age=60, name="John")
#
# # combination
# greet("John", age=60)
# greet(name="John", 60)    # SyntaxError
# greet("Sita", name="John")  # TypeError
# greet("Sita", age=30)


# positional only
# def add(a, /, b, c):
#     return a + b + c


# print(add(1, 2, 3))
# print(add(1, b=2, c=3))


# keyword only
# def add1(a, /, b, *, c):
#     return a + b + c


# print(add1(1, b=2, c=3))
# print(add1(a=1, b=2, c=3))
# print(add1(1, 2, 3))
# print(add1(a=1, b=2, c=3))

# variable number of positional arguments
# def add(*args):
#     print(args)
#     return sum(args)


# print(add(1, 2, 4))

# variable number of Keyword arguments

# def add(**kwargs):
#     print(kwargs)


# add(a=1, b=2, c=4)

# x = 12
#
#
# def add(a, b=x):    # default parameter
#     print(a + b)
#
#
# x = 10
# add(1)  # 13


# function annotations
def greet(name: str, age: int) -> str:
    print(f"hai {name}, your age is {age}")


greet("John", 30)   #
greet(12, 30)       #
greet("John", "30") #













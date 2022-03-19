def spam(func):
    def wrapper():
        print("hello everyone")
        func()      # display()
    return wrapper


@spam       # display = spam(display)
def display():
    print(1 + 2)


@spam       # display2 = spam(display2)
def display2():
    print(1 - 2)


# display = spam(display)     # func = display , display = wrapper
# display()
# display2 = spam(display2)
# display2()                  # func = display2, disply2 = wrapper

#######################################################################
# log decorator

import time

d = {}
# using normal dictionary
def log(func):
    def wrapper(*args, **kwargs):
        f_name = func.__name__
        if f_name not in d:
            d[f_name] = 1
        else:
            d[f_name] += 1
        res = func(*args, **kwargs)
        return res
    return wrapper

# using default dictionary
from collections import defaultdict
dd = defaultdict(int)

def log(func):
    def wrapper(*args, **kwargs):
        f_name = func.__name__
        dd[f_name] += 1
        res = func(*args, **kwargs)
        return res
    return wrapper

# using count
d = {}
def log(func):
    count = 0
    def wrapper(*args, **kwargs):
        f_name = func.__name__
        nonlocal count
        count += 1
        d[f_name] = count
        res = func(*args, **kwargs)
        return res
    return wrapper


@log     # @log
def add(a, b, c):
    return "adding 2 numbers:", a + b + c


@log
def sub(a, b):
    return a - b


# print(add(1, 2, c=3))
# print(add(1, 2, c=3))
# print(add(1, 2, c=3))
#
# print(sub(3, 9))
# print(sub(3, 9))
#
# # {add: 3, sub: 2}
# print(d)

###########################################################################
def n_times(n):
    def repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                res = func(*args, **kwargs)
                print(res)
        return wrapper
    return repeat

@n_times(3)
def add(a, b):
    return a + b

@n_times(2)
def sub(a, b):
    return a - b

add(11, 2)
sub(3, 1)


#######################################################################
def spam():
    return "hello"

start = time.time()
# print(start)
# print(spam())
# end = time.time()
# print(end - start)


""" assignment 

@ type_check(int, int, int)
def add(a, b, c):
    return a + b

add(1, 2, 3)
add("hai", 1, 2)

"""

def prime():
    for num in range(1, 20):
        if num > 1 and not any([num % 2 == 0 for i in range(2, num)]):
            yield num ** 3

print(list(prime()))










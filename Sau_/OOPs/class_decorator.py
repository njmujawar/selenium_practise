# >> getattr    =>  built-in-method, getting some attributes
# >> setattr    =>  built-in-method, setting some attributes
# ------------------------------------------------------------------------------------------------------------------- #

# Normal Function decorator

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#
#     return wrapper
# #
# #
# def logging(cls):                       # Class decorators should take class as an argument & modified that class
#     for key, value in cls.__dict__.items():
#         if callable(value):
#             setattr(cls, key, log(value))
#     return cls
#
#
# @logging                             # All the methods inside the class will be applied with the logging decorator
# class Arithmetic:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#
# a = Arithmetic(1, 2)
# print(a.add())

# # -----------------------------------------------------------------------------------------------------------------
#
#
# def prices(cls):
#     print("Attaching class Attribute")
#     # creates a class attribute by name "apple" on the class ShoppingCart
#     cls.apple = {"iphone": 900, "ipad": 2800, "imac": 4500}
#     return cls
#
#
# @prices
# class ShoppingCart:
#     def demo(self):
#         print(self.apple)
#
#
# # ------------------------------------------------------------------------------------------------------------------
#
# # Attaching an instance method to the class using class decorator
#
# def attach_init(cls):
#     def wrapper(self, a, b):
#         self.a = a
#         self.b = b
#     cls.__init__ = wrapper
#     return cls
#
#
# @attach_init
# class Arithmetic:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b

# from time import sleep
#
#
# class Decorate:
#     def __init__(self, func):
#         self.func = func
#         self.delay = 5
#
#     def __call__(self,*args, **kwargs):
#         # self.func = args
#         sleep(5)
#         res = self.func(*args,**kwargs)
#         return res
#         # return self.__init__.func(*args, **kwargs)
#
#
# @Decorate
# class Display:
#     def __init__(self, name):
#         self.name = name
#
#     def display(g):
#         print(g)
#
#
# # d = Display("SS")
# # d.display()
#
# d = Display.__call__([1, 2, 3])
# print(d)
# print(d.__dict__)


import time


class Delay:
    def __init__(self, func):
        self.func = func
        self.delay = 2

    def __call__(self, *args, **kwargs):
        time.sleep(self.delay)
        return self.func(*args, **kwargs)


@Delay
class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


a = Addition("S", "s")
print(a.add())
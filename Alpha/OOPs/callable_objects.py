# to print hello everyone msg

class Greeting:

    def __call__(self, name):
        print(f"hello {name}")


# g = Greeting()
# g("steve")

# check even or odd
class CheckEvenOdd:

    def __call__(self, num):
        if num % 2:
            return "number is odd"
        return "number is even"


c = CheckEvenOdd()
# print(c(8))
############################################################
# anagrams
class Anagrams:
    def __call__(self, string1, string2):
        if sorted(string1) == sorted(string2):
            return "strings are anagrams"
        return "strings are not anagrams"


a = Anagrams()
# print(a("desserts", "stressed"))

#############################################################

""" **************** class decorators ********************"""

# function decorator

def n_times(n):
    def outer(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper
    return outer


@n_times(4)
def horn_sound():
    print("pom")


# horn_sound()

# class decorator

class Ntimes:

    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                func(*args, **kwargs)
        return wrapper



@Ntimes(4)
def horn_sound():
    print("pom")

# horn_sound()

#####################################################################
def logging(msg="Good afternoon"):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(msg)
            func(*args, **kwargs)

        return wrapper
    return outer


@logging("hello there!!!")
def spam():
    print(2 + 3)


# spam()

class Logging:

    def __init__(self, msg="Good afternoon"):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(self.msg)
            func(*args, **kwargs)

        return wrapper

































































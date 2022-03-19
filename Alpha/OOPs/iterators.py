l = [1, 2, 3, 4]    # iterable
# print(next(l))

a = iter(l)
b = l.__iter__()
# print(b)

# print(next(b))
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())


# for i in b:
#     print(i)
#####################################
names = ["Roshan", "Dinesh", "Ravi", "Reddy", "SJ"]

# for name in names:
#     print(name)


class Sample:
    def __init__(self, iterable):
        self.names = iterable

    def __iter__(self):
        return iter(self.names)


s = Sample(names)
# print(dir(s))

# for name in s:
#     print(name)

########################################################################

names = ["Roshan", "Dinesh", "Ravi", "Reddy", "SJ"]

class Sample:
    def __init__(self, iterable):
        self.names = iterable
        self.iter_ = iter(self.names)

    def __iter__(self):
        return iter(self.names)

    def __next__(self):
        try:
            return next(self.iter_)
        except StopIteration:
            print("No elements")

s1 = Sample(names)

# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))

#######################################################


class Numbers:

    def __init__(self):
        self.start = 0
        self.end = 10

    def __iter__(self):
        return self

    def __next__(self):

        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            raise StopIteration


n = Numbers()

# for item in n:
#     print(item)

########################################################################
class Numbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):

        if self.start >= self.end:
            x = self.start
            self.start -= 1
            return x
        else:
            raise StopIteration


n = Numbers(10, 1)

# for item in n:
#     print(item)

################################################################################


l = ["flipkart", "amazon", "Myntra", "Meesho"]
#        0          1          2        3
class Reversed:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == -1:
            raise StopIteration
        else:
            x = self.index
            self.index -= 1
            return self.iterable[x]


r = Reversed(l)
# for i in r:
#     print(i)
l = [1, 2, 3, 4, 5]
class Squares:

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            res = self.iterable[self.index] ** 2
            self.index += 1
            return res
        else:
            raise StopIteration


sq = Squares(l)
# for i in sq:
#     print(i)

class Prime:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += 1
            if x > 1:
                for i in range(2, x):
                    if x % i == 0:
                        break
                else:
                    return x

        else:
            raise StopIteration


p = Prime(1, 50)
# for i in p:
#     if i:
#         print(i)


##########################################################################

class Fibonacci:

    def __init__(self, first, last):
        self.first = first
        self.next = first + 1
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if self.first > self.last:
            raise StopIteration
        else:
            a = self.first
            third = self.first + self.next
            self.first = self.next
            self.next = third
            return a

f = Fibonacci(1, 50)
# for i in f:
#     print(i)

print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))














































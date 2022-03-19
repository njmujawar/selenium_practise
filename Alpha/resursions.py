# count = 10
#
# while count > 0:
#     print(count)
#     count -= 1


def countdown(count):

    # if not count > 0:
    #     return

    print(count)
    countdown(count - 1)


# countdown(10)

# import sys
#
# print(sys.getrecursionlimit())
#
#
# sys.setrecursionlimit(2000)
#
# print(sys.getrecursionlimit())


n = 5
fact = 1

while n != 0:
    fact = fact * n
    n -= 1

# print(fact)

def factorial_(n, fact):

    if n == 0:
        return fact

    fact = fact * n

    return factorial_(n-1, fact)

# print(factorial_(5, 1))


# sum of first 10 numbers

sum = 0
n = 10

while n > 0:
    sum += n
    n -= 1

# print(sum)

def sum_10(n, sum=0):

    if n == 0:
        return sum

    sum += n
    return sum_10(n-1, sum)


# print(sum_10(10))


s = "hello"
i = 0
res = ""

while i < len(s):
    res = s[i] + res
    i += 1

# print(res)

def reverse_(s, i=0, res=""):
    if i == len(s):
        return res

    res = s[i] + res

    return reverse_(s, i+1, res)

# print(reverse_("hello"))

#######################################################################
# 0 , 1, 1
# , 2, 3, 5, 8, 13....

# elft@


# for row in range(3):
#     for col in range(row+1):
#         print("*", end=" ")
#     print()
#
# for row in range(1, 3):
#     print(f'{"* " * row:^8}')
# for row in range(3, 0, -1):
#     print(f'{"* " * row:^8}')
#
# pat = ""
# for char in range(ord("a"), ord("c")+1):
#     pat += chr(char) + " "
#     print(pat)

def add(a, b):
    return a + b


res = add(1, 2)
# print(res)

# lambda args: expression
total = lambda a, b: a + b
print(total(1, 2))




def add(a):
    return a + 20


res = add(1)


add = lambda a: a + 20
print(add(12))











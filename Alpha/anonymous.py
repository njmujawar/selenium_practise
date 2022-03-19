# # ############################### Lambda ################################
# # # square
# # square = lambda n: n ** 2
# # print(square(3))
# #
# # # cube
# # square = lambda n: n ** 3
# # print(square(3))
# #
# # # last item of an iterable
# # last_ele = lambda iterable: iterable[-1]
# # print(last_ele("hai"))
# #
# # # output of the expression a^2 + b^2 + 2ab
# #
# # res = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
# # print(res(1, 2))
# #
# # # even or odd
# # # x = int(input())
# # # even = lambda num: "even" if num % 2 == 0 else "odd"
# # # print(even(x))
# #
# # # palindrome
# # res = lambda string: "palindrome" if string.lower() == string.lower()[::-1] else "not palindrome"
# #
# # # print(res("Mom"))
# #
# # ###############################################################################
# l = [ 1, 2, 3, 4]
#
# # using lambda
# res = lambda n: n % 2 == 0
# # print(res(l))   # Error
#
# # using for loop
# output = []
# for item in l:
#     output.append(res(item))
#
# # using list comprehension
# output = [res(item) for item in l]
# # print(output)
#
# # using map
# m = map(res, l)
# # print(list(m))
#
#
#
# ###############################################################
# l = [1, 2, 3, 4, 5, 6]
# evens = lambda item: item % 2 == 0
#
# # using map
# res = list(map(evens, l))
# # print(res)      # [False, True, False, True, False, True]
#
# # using filter
# res1 = filter(evens, l)
# # print(list(res1))   # [2, 4, 6]
#
# ################################################################
l = [1, 2, 3, 4, 5, 6]

evens = lambda item: item % 2

res1 = filter(evens, l)
# print(list(res1))


#################################################################
names = ["eve", "Steve", "john", "ram", "sita"]

# def even_len(name):
#     return len(name) % 2 == 0

even_len = lambda name: name+"i"
# print(even_len("eve"))

res = filter(even_len, names)
# print(list(res))

###################################################################


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return 0

        else:
            return 1


prime = filter(is_prime, range(50))
# print(list(prime))

###############################################################################

nums = [1, 2, -2, -3, 4, -9, -2, 0, 5]

pos = list(filter(lambda n: n < 0, nums))
neg = list(filter(lambda n: n > 0, nums))

# print(sum(pos), sum(neg))
################################################################################
s = "hai how are you"

# using inbuilt function
def index_(string, ch):
    return (string.find(ch))


# print(index_(s, "z"))

# without using inbuilt function
s1 = "hai how are you"


def index_of_char(string, char):

    for index, item in enumerate(string):
        if item == char:
            return index


# print(index_of_char(s1, "z"))

"""
Write a function to print the below output.

func("TRACXN", 0)  # Should print RCN
func("TRACXN", 1)  # Should print TAX

"""

def func(string, n):
    if n == 0:
        return string[1::2]
    elif n == 1:
        return string[::2]


# print(func("TRACXN", 0))
# print(func("TRACXN", 1))

def last_digit(num):
    return int(str(num)[-1])


print(last_digit(1234))








# s = "hello"
#
# print(sorted(s))
#
# l = [12, 4, 5, 3, 6, 8, 7, 0]
# print(sorted(l))
#
# t = (12, 4, 5, 3, 6, 8, 7, 0)
# print(sorted(t))
#
# t = {12, 4, 5, 3, 6, 8, 7, 0}
# print(sorted(t))
#
# d = {"hai": 3, "are": 4}
# print(sorted(d))

##### custom sorting ##############

# 1. program to sort the list based on length of each name
names = ["john", "nikhil", "ravi", "mani", "shashi", "vidya", "dinesh"]

# print(sorted(names, key=len, reverse=True))


# program to sort based on the last character of each element
def last_item(element):
    return element[-1]

# print(sorted(names, key=last_item))

# using lambda function
# print(sorted(names, key=lambda item: item[-1]))

# program to sort based on the middle character of each element
names = ("john", "nikhil", "ravi", "mani", "shashi", "vidya", "dinesh")

res = sorted(names, key=lambda item: item[len(item)//2])
# print(res)

# sorting dictionaries
d = {"apple": 5, "google": 6, "walmart": 7, "flipkart": 7}

# sorting the dictionaries based on key's first character
# res = sorted(d)
# print(res)
#
# res1 = sorted(d.keys())
# print(res1)
#
# res2 = sorted(d.items())
# print(dict(res2))

# sorting the dictionaries based on key's last character

d = {"apple_products": 5, "google_search": 6, "walmart": 7, "flipkart": 7}

op1 = sorted(d, key=lambda item: item[-1])
# print(op1)
#
op2 = sorted(d.keys(), key=lambda item: item[-1])
# print(op2)

# print(d.items())
op3 = sorted(d.items(), key=lambda item: item[0][-1])
# print(op3)

# sorting values in a dictionary

d = {"apple_products": 5, "walmart": 8, "google_search": 6, "flipkart": 7}

res1 = sorted(d.values())
# print(res1)

res2 = sorted(d.items(), key=lambda item: item[-1])
# print(res2)

# sort based on last character of each element
items = ['bv', 'aw', 'dt', 'cu']
sorted(items, key=lambda item: item[-1])

# sort based on the temperatures of each city
temp = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

# [('Bangalore', 25), ('Mumbai', 32), ('Delhi', 35), ('Chennai', 37)]
# min_, *rest, max_ = sorted(temp, key=lambda item: item[-1])
# print(min_)
# print(max_)

# min_ = min(temp, key=lambda item:item[-1])
# print(min_)

# max_ = max(temp, key=lambda item:item[-1])
# print(max_)

# sort based on the first value of the inner list
items = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]

op = sorted(items)
# print(op)

# sort based on the share prices and get the maximum share price with its name
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }


# *rest, max_ = sorted(prices.items(), key=lambda item: item[-1])
# print(max_)

# write a program to get the most repeated word in the below sentence
sentence = "hi how are you how is your health"

a = sentence.split()
d = {item: a.count(item) for item in a}
# print(d)

# *rest, max_ = sorted(d.items(), key=lambda item: item[-1])
# print(max_)

# program to print the longest non repeated word in the sentence
s = "python is a programming language and programming is fun"
a = s.split()
d = {item: len(item) for item in a if a.count(item) == 1}
# print(d)

shortest, *rest, longest = sorted(d.items(), key=lambda item: item[-1])
# print(longest, shortest)


students = [
    {"name": "john", "grade": "A", "age": 26},
    {"name": "jane", "grade": "B", "age": 28},
    {"name": "dave", "grade": "B", "age": 22}
]

# sorting based on age
print(sorted(students, key=lambda item: item["age"]))

# sorting based on name
print(sorted(students, key=lambda item: item["name"]))

def type_check(a, b):
    pass



@type_check(int, str)
def add(a, b):
    return a + b


print(add(1, 2))



















































# for _ in range(5):
#     print("hai", end=" ")

################################################################
# print(list(range(1, 6)))

# for i in range(1, 6):
#     print(i ** 2)


##################################################################
# for i in range(0, 11, 2):
#     print(i)


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

##################################################################
# for i in range(21, 40):
#     if i % 2 != 0:  # if i % 2:     if not i% 2 == 0:
#         print(i)

#################################################################
# for i in range(1, 50):
#     if i % 4 == 0 and i % 7 == 0:
#         print(i)

##################################################################
# n = 6
# flag = 0
#
# for i in range(2, n):
#     if n % i == 0:
#         flag = 1
#         break
#
# if flag == 0:
#     print("It is a prime")
# else:
#     print("It is not a prime")


# for n in range(2, 50):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#
#     else:
#         print(n, end=" ")


# i = 0
# count = 0
#
# while count < 10:
#
#     if i % 2 == 0:
#         print(i)
#         count += 1
#
#     i += 1

###################################################
# s = "hello"
#
# for item in range(len(s)):
#     print(item, s[item])
#
# print()
# print("using sequence")
# for item in s:
#     print(s.index(item), end=" ")
#     print(item)


# list_= ["apple"]
# for i in list_:
#     if list_ == []:
#         print("empty list")
#     else:
#         print("not empty")

#############################################################
# a = "hello"
#
#
# # using range
# for item in range(len(a)):
#     print(item, a[item])
#
# # using enumerate - unpacking inside for loop
# for item in enumerate(a):
#     print(item[0], item[1])
#
# # using enumerate - unpacking in for loop definition
# for index, item in enumerate(a):
#     print(index, item)

###################################################################
# d = {"a": "apple", "b": "ball", "c": "cat"}


# for key in d:
#     print(d[key])
#
# for val in d.values():
#     print(val)
#
# for key, value in d.items():
#     print(value)

###################################################################
# a = ["hai", "hello", "welcome"]
# b = [3, 5, 7]
#
# for item1, item2 in zip(a, b):
#     print(item2)

###################################################################
s = "hello"
d = {}

for item in range(len(s)):
    d[item] = s[item]
# print(d)

d1 = {}

for index, item in enumerate(s):
    d1[index] = item

# print(d1)

d2 = dict(enumerate(s))
# print(d2)

####################################################################
l = [12, 3, 4, 5, 8]
res = []

for index, item in enumerate(l):
    a = item ** index
    res.append(a)

# print(res)

#######################################################################

string = "hello world"

d = {}

for char in string:
    if char in "aeiouAEIOU":
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

# print(d)


string = "hello world"

d = {}

for char in string:
    if char.lower() in "aeiou":
        d[char] = string.count(char)


##################################################################

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res =[1, 2, 3, 4, 5, 6, 7, 8, 9]

res = []
for i in l:    # [1, 2, 3]
    for j in i:
        res.append(j)

print(res)

res1 = [j for i in l for j in i]
print(res1)


















































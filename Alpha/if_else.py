# x = input("enter the value of x: ")
# y = input("enter the value of y: ")
#
# a = int(x)
# b = int(y)
#
# if a > b:
#     print("x is greater")

###########################################################
# x = int(input("enter the value of x: "))
# y = int(input("enter the value of y: "))

# if x > y:
#     print("x is greater")
#
# else:
#     print("y is greater")

###########################################################

# inline if statement
# if x > y: print("x is greater")

#   if block    if condition else else block

# print("x is greater" if x > y else "y is greater")

#########################################################

# x = int(input("enter the value of x: "))
# y = int(input("enter the value of y: "))
# z = int(input("enter the value of z: "))

# if x > y:
#     print("x is greater than y")
#
# elif x > z:
#         print("x is greater than z")

############################################################3
# a = 12
# b = 23
# c = 20
#
# if a > b and a > c:
#     print("a is greater")
#
# elif b > c:
#     print("b is greater")
#
# else:
#     print("c is greater")

############################################################
"""
ch = input
"a" ch "z"  --> ord(ch) - 32
" A" ch "Z" --> ord(ch) + 32
"""

# ch = input("enter a character: ")
#
# if "a" <= ch <= "z":
#     print(chr(ord(ch) - 32))
#
# elif "A" <= ch <= "Z":
#     print(chr(ord(ch) + 32))
#
# else:
#     print("It is not an alphabet")

# ###########################################
# ch = input("enter a character: ")
# # print(ch.swapcase())
#
# if ch.islower():        # bool(h.islower()) ==> bool(True)
#     print(ch.upper())
#
# else:
#     print(ch.lower())


# s = ""
#
# if len(s) != 0:
#     print("string is not empty")
# else:
#     print("string is empty")

###########################################################
# s = ""
# if bool(s):
#     print("string is not empty")
# else:
#     print("string is empty")

###########################################################
# s = ""
# if s:
#     print("string is not empty")
# else:
#     print("string is empty")

#############################################################
# char = input("enter a character: ") # "a"
# d = {}
#
# if char.lower() in "aeiou":
#     d[char] = ord(char)


# print(d)
###############################################################
# d = {"a": 1, "b": 2}
# key = input("enter the key: ")
#
# if key in d:
#     d[key] += 1
#
# else:
#     d[key] = 1

# print(d)

###########################################################
# a = ("hai",)
#
# if isinstance(a, str):
#     print("a is string")
#
# else:
#     print("a is not a string")

#############################################################

# number = int(input("enter the number: "))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# print(f"{number} is even" if number % 2 == 0 else f"{number} is odd")

###############################################################

num = 1221


# if str(num)[::-1] == str(num):
#     print(f"{num} is a palindrome")
# else:
#     print(f"{num} is not a palindrome")

###################################################################
# year = 2012
#
# if year % 4 == 0 and year % 100 != 0:   # non century years
#     print(f"{year} is a leap year")
#
# elif year % 400 == 0:       # century years
#     print(f"{year} is a leap year")
#
# else:
#     print(f"{year} is not a leap year")
#
#
#
# import calendar
#
# print(calendar.isleap(2100))

##########################################################
# a = 15
# b = round(a ** 0.5)
#
# if b ** 2 == a:
#     print(f"{a} is a perfect square")
# else:
#     print(f"{a} is not a perfect square")

#######################################################3##
# char = input("enter some character: ")
#
# if "a" <= char <= "z" or "A" <= char <= "Z":
#     print("It is an alphabet")
#
# elif "0" <= char <= "9":
#     print("It is a number")
#
# else:
#     print("It is a special character")

##############################################################
# marks = int(input("enter the marks: "))

# if 35 <= marks < 60:
#     print("pass")
#
# elif marks >= 60:
#     print("first class")
#
# else:
#     print("fail")

#############################################################
# s = "ai"
#
# if s[-1].lower() in "aeiou":
#     print(f"{s} is ending with a vowel")
#
# else:
#     print(f"{s} is not ending with a vowel")

###############################################################
# l = [1, 2, 3, 4, 5]
#
# if len(l) % 2 == 0:
#     print(" The list has even numbered elements")
# else:
#     print("The list has odd numbered elements")

###############################################################
n = 123










































































































































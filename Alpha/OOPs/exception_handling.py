# default except block

# a = 10
# b = 0
#
# try:
#     c = a / b
#     [1, 2, 3].extend(10)
#     print(c)
#
# except:
#     print("Exception is handled")

##################################################################
# specific except block

# a = 10
# b = 0
#
# try:
#     [1, 2, 3].extend(10)
#     c = a / b
#     print(c)
#
# except (ZeroDivisionError, TypeError):
#     print("ZeroDivisionError is handled")

# except TypeError:
#     print("TypeError is handled")
##################################################################

# generic except block

# a = 10
# b = 0
#
# try:
#     c = a / b
#     [1, 2, 3].extend(10)
#     print(c)
#
# except ZeroDivisionError as msg:
#     print(msg)
#     print("Exception is handled")
#
# else:
#     print("execution done")

# a = int(input("enter a number: "))
#
# if a != 0:
#     c = 10 / a
#     print(c)
#
# else:
#     raise ValueError("the number is zero")

# custom exception
class AgeError(Exception):
    pass


# main program
# age = int(input("enter your age:"))
#
# if age > 18:
#     print("You are eligible")
#
# else:
#     raise AgeError("Please grow up and wait till you turn 18")


names = ["apple", "google", "yahoo", "yahoo", "gmail", "apple", "apple", "apple"]
d = {}

for name in names:
    try:
        d[name] += 1
    except KeyError:
        d[name] = 1

# print(d)

##################################################################################

data = ["apple", 12, "yahoo", "gmail", [1.5, 2+3j], 1345, 90.69]

# for ele in data:
#     try:
#         print(ele[0])
#     except TypeError:
#         print("The element is not a sequence")

#############################################################################
f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample.txt"

# with open(f_path) as f:
#     for line in f:
#         try:
#             a = line.split()[0]
#         except IndexError:
#             print("Line is empty")
#         else:
#             print(a)




































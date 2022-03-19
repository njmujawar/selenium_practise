# a = input("enter the value of a: ")
# b = input("enter the value of b: ")
# # print(a, b, sep="*")
# print(a, end="*")
# print(b)

# a = "Ram"
# b = 10
# print("My name is", a, end=",", sep="$$")
# print("I am", b, "years old", sep="$$")

# print("hai", "hello", sep="-", end=",")
# print("welcome", "everyone", sep=":")

# s = r"hai \naveen welcome \to \the class"
# print(s)

# a = r"\\\"
# print(a)

year = 2600

if year % 4 == 0 and year % 100 != 0:
    print("leap year")

elif year % 400 == 0:
    print("leap year")

else:
    print("not a leap year")



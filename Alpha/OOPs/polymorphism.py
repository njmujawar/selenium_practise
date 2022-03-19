# w.r.t inbuilt function

s = "hai"
# len(s)  # charcters

# l = [1, 2, 3, 4, 5]
# len(l)  # no of elements
#
# t = (1, 2, 3, 4, 5)
# len(t)  # no of elements
#
# s = {12, 3,4 ,5, 6}
# len(s)  # no of keys
#
# d = {"a": 1, "b": 2}
# len(d)  # no of keys

#######################################################

# w.r.t operators

# # addition operator
# print(1 + 2)    # 3
# print("1" + "2")    # 12

# subtraction
# print(1 - 2)    # -1
# print({1, 2} - {2, 3, 4})  # 1

# multiplication

# print(2 * 3)    # 6
# print([1, 2, 3] * 2)


# methods

class SBI:

    def balance(self):
        print("in SBI balance")

    def withdraw(self):
        print("in SBI withdraw")


class ICICI:
    def balance(self):
        print("in ICICI balance")

    def withdraw(self):
        print("in ICICI withdraw")


sbi = SBI()
icici = ICICI()

objects = (sbi, icici)

# for obj in objects:
#     obj.balance()
#     obj.withdraw()


class Bank:

    def balance(self):
        print("in SBI balance")

    def withdraw(self):
        print("in SBI withdraw")


class ICICI(Bank):
    def balance(self):
        print("in ICICI balance")
        super().balance()

    def withdraw(self):
        print("in ICICI withdraw")
        super().withdraw()

b = Bank()
b.balance()
i = ICICI()
i.balance()
































































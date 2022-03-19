# even =lambda num: num%2 == 0
# print(even(3))
# multiply = lambda num1,num2: num1*num2
# print(multiply(2,3))
# last = lambda sequence: sequence [-1]
# print(last(["hi","m","ji","21"]))
# sent = lambda pala: pala == pala [::-1]
# print(sent("mom"))
# sent  = lambda pala :pala ==pala[::-1]
# print(sent("tot"))
# sentence  = lambda num1,num2: print (f"{num1} is greater") if num1>num2 else print(f"{num2}is greater")
# sentence(7,8)

# l1 = ["Tom", "Jerry", 26, 15, 31.5, 3+5j, 7]
# l = [element for element in l1 if isinstance(element, int)]
# l = [1, 2, 3, 4, 56, 6]
# def even_odd(num):
#     if num % 2 == 0:
#         return f'{num} is even'
#     return f'{num} is odd'
#
#
# output = map(even_odd, l)
# print(list(output))
#
# print(l)
# k = [element for element in l1 if isinstance(element,(int , float ))]
# print(k)
# l = ["apple", "gmail", "yahoo", "flipkart", "instagram"]
# def vowel(item):
#     if item[0] in "a,e,i,o,u":
#             return item
# k =map(vowel,l)
# print(list(k))
#
# vowevls = lambda item :item[0] in "a,e,i,o,u"
# e =map(vowevls,l)
# print(list(e))
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
def add_(item1,item2):
    return  item1 + item2
m = map(add_,a,b)
print(list(m))


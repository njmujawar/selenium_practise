from selenium import webdriver
driver = webdriver.Firefox()
# driver.get('https://www.flipkart.com/')
# s ="hello  python"
import socket
# from collections import defaultdict
# dd = defaultdict(int)
# for char in s:
#     dd[char] += 1
# # print(dd)
# dd = defaultdict(int)
# for char in s:
#     dd[char] += 1
# print(dd)
# p = {char: s.count(char) for char in s}
# print(p)
# names = ["apple", "google", "apple", "yahoo", "yahoo", "google", 'gmail', 'gmail', 'gmail']
# dd = defaultdict(list)
# for index,item in enumerate(names):
#     dd[item] += [index]
# print(d)
# files = ["apple.txt", 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']
# d = defaultdict(list)
# for item in files:
#     l = item.split(".")
#     d[l[-1]] += [item]
# print(d)
# s = {"a": 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# d ={}
# for item,value in s.items():
#     if isinstance(value,str):
#         d[item] = value[::-1]
#     else:
#         d[item] = value
# print(d)
# print({item: values[::-1] if isinstance(values, str) else values for item, values in d.items()})
# languages = ["Python", "Java", "Perl", "PHP", "Python", "JS", "C++", "JS", "Python", "Ruby"]
# lis = []
# for item in languages:
#     if item[0] in "pP":
#         lis.append(item)
# print(lis)
# res = []
# _list = [item for item in languages if item[0] in "pP"]
# print(_list)
# for item in languages:
#     if item not in res:
#         if len(item) == 6:
#             res.append(item)
# print(res)
# a = [1, 2, 3, 4, 5]
# k = []
# for index,item in enumerate(a):
#     b = item**index
#     k.append(b)
# print(k)
#
#
# a = [1, 2, 3, 4, 5]
#
# list_ = [item ** index for index, item in enumerate(a)]
# print(list_)
# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
# p = []
# for item in names:
#     a = (item ,len(item))
#     p.append(a)
# print(p)
# k = [(item,len(item)) for item in names]
# print(k)
# items = ["apple", 1.2, 'google', '12.6', 26, '100']
# a = []
# for item in items:
#     if isinstance(item,(int,float)):
#         a.append(item)
    # else:
    #     pass
# print(a)
# a = [item for item in items if isinstance(item,(float,int))]
# print(a)
# items = ["apple", 1.2, 'google', '12.6', 26, '100']
# p = []
# k = 2
# for i in range(k):
#     s = items.pop()
#     items.insert(0,s)
#
#
# print(items)
# numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
# k =[]
# num_ = max(numbers)
# for item in (numbers):
#     if item == num_:
#         k.append(item)
# print(k)
# p = [item for item in numbers if item == num_]
# print(p)
# k = [num for num in range(1,50) if num%2 ==0]
# print(k)\
# k = []
# for i in range(1,50):
#     if i%2 ==0:
#         k.append(i)
# print(list(k))
# names = [("apple", "google", "apple", "yahoo", "yahoo", 'google', 'gmail', 'gmail', 'gmail']
from collections import defaultdict
# dd = defaultdict(list)
# names = [("apple", "google", "apple", "yahoo", "yahoo", 'google', 'gmail', 'gmail', 'gmail'

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# for key,value in d.items():
#     if isinstance(value,str):
#         dd[key].append(value[::-1])
#     else:
#         dd[key] += [value]
# print(dd)


# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
# dd = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(dd)
""" 3. WAP to get all the duplicate items & the number of time the item is repeated in the list """

# names = ["apple", "google", "apple", "yahoo", "yahoo", 'google', 'gmail', 'gmail', 'gmail']
# dd = defaultdict(int)
# for item in names:
#     dd[item] += 1
# d = {item: names.count(item) for item in names}
# print(d)

# dd = defaultdict(str)
# cities = ["Tokyo", "Delhi", "Shanghai", "Sao-Paulo", "Mumbai"]
# population = ["38,001,00", '25,703,168', '23,740,778', '21,066,245', '21,042,538']
# for city,populations in zip(cities,population):
#     dd[city] = populations
# print(dd)
# dd= defaultdict()
# d= {"a": "hello", "b": 100, "c": 10.1, "d": "world"}
# for v,k in d.items():
#     a = v
#     b = k
#     dd[b] = a
# print(dd)
# t = {v:k for k,v in d.items() }
# print(t)
""" 6. Group even & odd index values with comprehension """
# l = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7, 8, 8, 8, 88, 99, 100]
#
# Method 1:
# e_index = [l[index] for index in range(0, len(l), 2)]
# o_index = [l[index] for index in range(1, len(l), 2)]
# list_ = [e_index, o_index]
# a = ["even", "odd"]
# d = {i: j for i, j in zip(a, list_)}
# print(d)
# print(e_index)
# print(o_index)
D = {"names": "apple", "ID": 152778}
d = {"helo": "apple", "Ib": 657678}
dd = {k1: [D[k1], d[k2]] for k1, k2 in zip(D, d)}
print(dd)
a =zip(D,d)
print(list(a))






















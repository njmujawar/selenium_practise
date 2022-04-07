from selenium import webdriver
# driver = webdriver.Firefox()
driver = webdriver.Chrome(".\chromedriver")
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
# D = {"names": "apple", "ID": 152778}
# d = {"helo": "apple", "Ib": 657678}
# dd = {k1: [D[k1], d[k2]] for k1, k2 in zip(D, d)}
# print(dd)
# a =zip(D,d)
# print(list(a))

# import re
# s = " hello ana world  annna '45415454564'"
# t = "annnnaaa"
# k = re.findall('\d{5}^', s)
# print(k)
# print(len(k))
# re.findall("a.")
# /////////////////////////////////////////////////////////////////////////////////////////
# a = ["hi", "babe","hello","hey","mom"]
# def count_(string , count = 0):
#     for _ in string:
#         count +=
#     return count
# print(count_(a))
#///////////////////////////////////////////////////////////////////////////////////////
# mmm = "hi how are you hi how  hi hi "
from collections import defaultdict
# def dictionary_(cc):
#     dd = defaultdict(int)
#     l = cc.split()
#     for word in l:
#         dd[word] += l.count(word)
#     return dd
# print(dictionary_("hi how are you you you"))
# print(a)


# l = "hi how are you hi how  hi hi "
# words = l.split()
# l1 =[]
#
# def count_():
#     for word in words:
#         l.count(word)
#     return
# print(count_("hi how are you hi how  hi hi "))
# sentence = "hi how are you hi how  hi hi "
# from collections import defaultdict
# d = defaultdict(int)
# words = sentence.split()
# for word in words:
#     d[word] += words.count(word)
# print(d)
# s = "python is a language, python programming is easy"
# s1= s.split()
# d = {word: s1.count(word) for word in s1 if len(word) % 2 == 0}
# print(d)
import re
# s = 'python is a programming language  python and programming python is fun'
# a = re.search("python", s)
# print(a)
#
# s = """python Java is a programming language. programming is fun. python is easy"""
# c = re.match("python", s)
# print(c)
# mobile_num = ["1234456789", "9876543210", "6547893210", "56732456840"]
# for num in mobile_num:
#     print(re.findall("^[6-9]\d{9}$", num))
#///////////////////////////////////////////////////////////////////////////////////////
import re
# d = {"hello": 2 , "hi": 5 , "yes": 9}
# b = (max(d.items(), key=lambda item:item[1])[1])
# print(b)
# //////////////////////////////////////////////////////////////////////////////////////
from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# from PIL import Image
# from Screenshot import Screenshot_Clipping
# driver.get(r'https://www.google.com/')
# sleep(5)
# driver.save_screenshot('abcd.png')
# s = Image.open('abcd.png')
# s.show()
#/////////////////////////////////////////////////////////////////////////////////////////////
# square = lambda n: n**2
# print(square(3))
# last_ele  = lambda iterable : iterable [-1]
# print(last_ele('123'))

# res = lambda a , b : a**2 + b**2 + 2 * a * b
# print(res(2,3))
# even  = lambda num : "even" if num%2 == 0 else "odd"
# print(even(4))
# res = lambda string : "paladrom " if string.lower() == string.lower()[::-1]  else"not pala"
# print(res("hia"))
# l = [1,2,3,4]
# res = lambda n : n % 2 == 0
# d = []
# for item in l:
#     if item %2 ==0:
#         d.append(item)
# k = filter(res,l)
# print(list(k))
# driver.get('http://demowebshop.tricentis.com/register')
# sleep(3)
# driver.find_element_by_xpath("(//input[@name='Gender'])[1]").click()
# links = driver.find_elements_by_xpath("//div[@class='block block-category-navigation']//a")
# for link in links:
#     print(link.text)
# sleep(2)
# b = []
# links = driver.find_elements_by_xpath("//div[@class='footer-menu-wrapper']//a")
# for link in links:
#     b.append(link.text)
# print(b)
# print(len(b))
# sleep(2)
driver.get("https://www.myntra.com/kids?f=Categories%3ATshirts%3A%3AGender%3Aboys%2Cboys%20girls&plaEnabled=false")
sleep(3)

disc_pr = driver.find_elements_by_xpath("//span[@class='product-discountedPrice']")
disc_prices =[item.text for item in disc_pr]

tshirts = driver.find_elements_by_xpath("//div[@class='product-productMetaInfo']/.//h4[@class='product-product']")
t_shirts =[item.text for item in tshirts]

actual_disc=[]
for name,discount in zip(t_shirts,disc_prices):
    actual_disc.append((name,discount))
print(actual_disc)
result = sorted(actual_disc,key=lambda item:item[-1])
print(result)
print(result[-1:-7:-1])
import re
res = []
for item in actual_disc:
    item1,item2 = item
    # result = re.findall(r"[0-9]", item2)
    result =  item2
    res.append(result)
    # res.append("".join(result))
#
print(res)
print(res[-1:-7:-1])

# first, *rest, last = result
# print(first,last)

# print(result[-1:-7:-1])
#
# print(len(result[-1:-7:-1]))















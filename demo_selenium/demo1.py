from selenium import webdriver
driver = webdriver.Firefox()
import time
from time import sleep
# driver.get('http://demowebshop.tricentis.com/')
# sleep(3)
# driver.find_element_by_id("small-searchterms").send_keys("hello")
# sleep(3)
# driver.find_element_by_xpath("//input[@class='button-1 search-box-button']").click()
# sleep(3)
# driver.back()
# driver.close()
# print("Banglore "* 10)
# string = "hai1234python23"
# _alpha = 0
# _digit = 0
#
# for char in string:
#     if char.isalpha():
#         _alpha += 1
#     elif char.isdigit():
#         _digit += 1
# print(f"this is alpha= { _alpha}")
# print(f"This is digit={ _digit}")
# string = "hai1234python23"
# _alpha = 0
# _digit = 0
# for char in string:
#     if "a"<= char <="z":
#         _alpha += 1
#     if "0" <= char <= "9":
#         _digit += 1
# print(_alpha)
# print(_digit)
# string = "a jjnJHa e iNNlm"
# res = ""
# for char in string:
#     if "a"<= char <="z":
#         res += chr(ord(char)-32)
#     elif "A"<=char<="Z":
#         res += chr(ord(char)+32)
#     else:
#         res += char
# print(res)
# res = ""
#
# for char in string:
#     if char.isupper():
#         res += char.lower()
#     elif char.islower():
#         res += char.upper()
#     else:
#         res += char
# print(res)
# res = ""
# for char in string:
#     if char.isalpha() and char not in "aeiou":
#         res += char
# print(res)
# string = "Million Dollar Smile"
# res = ""
#
# # # Method 1:
# for char in string:
#     if char.isalpha() and char not in "aeiouAEIOU":
#         print(char, end=" ")
# s  =  "programming"
# woord = "m"
# for dd,char in enumerate(s):
#     if char== woord:
#         print(dd)
# for i in enumerate(s):
#     print(i)
# for char in s:
#     if char == woord:
#         print(char,s.index(woord))
# for char in s:
#     if char.lower() in "aeiou":
#         print(char , ord(char))
# s ="iohufuokjlmj jkjhfoiw3jkl "
# count =0
# for i in s:
#     count += 1
# print(count)
# names = ['apple', "google", "apple", "yahoo", "google"]
# l = []
# for item in names:
#     if item not in l:
#         l.append(item)
# print(l)
# for item in names:
#     if names.count(item) ==1:
#         l.append(item)
# print(l)
# print(set(names))
# items = ['apple', 1.2, "google", "12.6", 26, "734"]
# l = []
# p = [item for item in items if isinstance(item,(int,float,complex))]
#
# print(p)
# sentence = "hello 123 world 567 welcome to 9724 python"
# sum_ = 0
# Method 1:
# for char in sentence:
#     if char.isdigit() and int(char) % 2 == 0:
#         sum_ += int(char)
#
# print(f"Sum of all even numbers are {sum_}")
# _sum = 0
# for item in sentence:
#     if item.isdigit() and int(item) % 2==0:
#         _sum += int(item)
# print(_sum)
# import pickle
# k = []
# languages = ["Python", "Java", "Perl", "PHP", "python", "JS", "c++", "JS", "python", "ruby"]
# p = [element for element in languages if element[0] in "pP"]
# for item in p:
#     if item not in k:
#         k.append(item)
# print(k)
# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
# print([item for item in names if len(item) % 2 ==0])
# names = ["apple", "google", "yahoo", "facebook", "yelp", "flipkart", "gmail", "instagram", "microsoft"]
# l = []
# t =[]
# for item in names:
#     if len(item)%2 ==0:
#         l.append(item)
#     else:
#         t.append(item[::-1])
# print(l)
#
# print(t)
# l = []
# for num in range(1,101):
#     if num >1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
            # l.append(num)
# print(l)
# l = []
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#          else:
#             l.append(num)
#
# print(l)
# item = ['apple', "1.2", 'google', "12.6", "26", '100']
# k =2
# for items in range(k):
#     remove_element = item.pop()
#     item.insert(0,remove_element)
# print(item)
n = 30

#
# def fibo(num, a=0, b=1):
#     if a <= num:
#         print(a, end=" ")
#         c = a + b
#         return fibo(num, a=b, b=c)
#
#
# fibo(n)


""" WAP to check if the given element is present in the collection or not """

""" WAP to check if the given element is present in the collection or not """
# list_ = ["Python", "Java", "SQL", "Selenium"]
# element_ = "V"
#
#
# def func(iterable, element):
#     for i in iterable:
#         if i == element:
#             return f'{i} is present inside the list'
#         return f'{i} is not present inside the list'
#
#
# print(func(list_, element_))

l = ["gmail", "flipkart", "google", "yahoo", "rediff"]
#
# odd_length = lambda item: len(item) % 2 != 0
#
# res = filter(odd_length, l)
# print(tuple(res))


# l = [10, 20, 30, 40, 40]


# def even_square(item):
#     if item[0] % 2 == 0:
#         return item[1] ** 2
#
#
# res = list(filter(even_square, enumerate(l)))
# print(list(map(even_square, res)))
# # print(res)
# //////////////////////////////////////////////////////////////////////////////
# driver.get('https://www.ajio.com/men-casual-shoes/c/830207006')
# sleep(4)
#
# element_shoe = driver.find_elements_by_xpath("//div[@class='nameCls']")
# element_price = driver.find_elements_by_xpath("//span[@class='price  ']")
#
# shoe_name  = [item.text for item in element_shoe]
# shoe_price = [item.text for item in element_price]
# prices =[]
# import re
# for price in shoe_price:
#     match = re.findall(r'\d',price)
#     prices.append(int(''.join(match)))
# print(shoe_price)
# pairs = []
# for shoe, price in zip(shoe_name,prices):
#     pairs.append({"name": shoe,"price" :price})
#
# max_price = sorted(pairs,key= lambda item:item["price"])[-1]
# min_price = sorted(pairs,key= lambda item:item["price"])[0]
# print(max_price,min_price)
# print(pairs)
#
# ///////////////////////////////////////////////////////////////////////////////////////////
# *
# * *
# * * *
# * * * *
# for row in range(4):
#     for col in range(row+1):
#         print("*", end=" ")
#     print()
# ///////////////////////////////////////////////////////////////////////////////////////////
# for row in range(1,5):
#     print("* " * row)
# //////////////////////////////////////////////////////////////////////////////////////////
#       *
#     * *
#   * * *
# * * * *

# for row in range(1,5):
#     print(f'{"* "* row:>8}')
# //////////////////////////////////////////////////////////////////////////////////////////
#    *
#   * *
#  * * *
# * * * *
#
#
# for row in range(1,5):
#     print(f'{"* " * row:^8}')
# //////////////////////////////////////////////////////////////////////////////////
# * * * *
#   * * *
#     * *
#       *
# for row in range(4,0,-1):
#     print(f'{"* "* row :>8}')
# ////////////////////////////////////////////////////////////////////////////////////
# a
# a b
# a b c
# a b c d
# x = ""
# for row in range(ord("a"),ord("d")+1):
#     x += chr(row) + " "
#     print(x)
#  ////////////////////////////////////////////////////////////////////////////////pat
import xlrd

# path =r"C:\Users\asd\Desktop\Sample.xlsx"
# l = [1,2,2,2,5,3,5,6]
# res = []
# b = []
# for i in l:
#     if l.count(i)>1:
#         res.append(i)
#
#     else:
#         b.append(i)
#
#
# print(b)
# print(set(res))
#////////////////////////////////////////////////////////// ////////////////////////////////////////////////
driver.get("https://www.ajio.com/")
driver.find_element_by_xpath("//input[@placeholder='Search AJIO']").send_keys("shoe")
driver.find_element_by_xpath("//span[@class='ic-search']").click()




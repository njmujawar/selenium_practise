def spam():
    yield "hai"
    yield 1
    yield 2


res = spam()
# print(res)
# print(list(res))
# print(len(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

l = [1, 2, 3, 4]
squares = []

""" using regular function"""
def squares_():
    for item in l:
        squares.append(item ** 2)
    return squares


res = squares_()
# print(res)

""" list comprehension """
squares1 = [item ** 2 for item in l]
# print(squares1)


""""""
squares2 = (item ** 2 for item in l)
# print(list(squares2))

# for i in squares2:
#     print(i)

""" using yield keyword"""

def squares_():
    for item in l:
        yield item ** 2


# for item in squares_():
#     print(item)

# res = squares_()
# print(res)      # gen obj
# print(list(res))    # [1, 4, 9, 16]
#
# res = squares_()
# print(next(res))    # 1
# print(next(res))    # 4
# print(next(res))    # 9
# print(next(res))    # 16

f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample2.txt"


def read_line(filepath):
    with open(filepath) as f:
        for line in f:
            yield line


res = read_line(f_path)
print(next(res))


with open(f_path) as file:
    def lines():
        for line in file:
            yield line


    res = lines()
    print(list(res))








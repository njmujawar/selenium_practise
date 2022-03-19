from collections import Counter

# f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample.txt"
#
# # without context manager
# f_obj = open(f_path, "r")
# # print(f_obj.closed)     # False
# # print(f_obj.mode)
# # print(f_obj.name)
#
# f_obj.close()
# # print(f_obj.closed)     # True
#
#
# # using context manager
# # with open(f_path) as f:
# #     print("in file", f)
# #     print(f.closed)     # False
#
# # print(f.closed)     # True
# ############################### file attributes
f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample.txt"
#
# # with open(f_path, "r+") as f_obj:
# #     print(f_obj.readable())
# #     print(f_obj.writable())
#
# ##############################################################
# """             reading from a file             """
#
# with open(f_path) as f:
#     data = f.read(4)    # reads only 4 characters
#     print(data)
#
# with open(f_path) as f:
#     data = f.readline(4)    # reads 4 characters from first line
#     print(data)
#     data = f.readline(4)    # reads 4 characters from second line
#     print(data)
#     data = f.readline(10)   # reads 10 characters from the third line
#     print(data)
#     """ readline() reads only one line at a time and if the specified integer exceeds the
#     number of characters in the line, then it will never go to the next line unless
#     it is called again"""
#
# with open(f_path) as f:
#     data = f.readlines(15)
#     print(data)
#     """
#     readlines() reads the entire sentence if the specified integer is in between the length of
#     the line. If it exceeds the length then the next line will be read.
#     """




# with open(f_path) as f:
#     data = f.read()
#     print(data)
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     data = f.readline()
#     print(data)
#
# with open(f_path) as f:
#     data = f.readlines()
#     print(data)
#
# with open(f_path) as f:
#     for line in f:
#         print(line)


""" writing into a file """

# with open(f_path, "a") as f:
#     print(f.write("hello"))
#     print(f.writelines(["hai\n", "hello\n", "python\n"]))


# count the number of words present in the file
f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample.txt"
with open(f_path) as f:
    count = 0
    for line in f:
        a = line.split()
        count += len(a)
    # print(count)

# count the number of lines in the file
with open(f_path) as f:
    count = 0
    for line in f:
        count += 1
    # print(count)

# print line and line number

# with open(f_path) as f:
#     for line_no, line in enumerate(f, start=1):
#         if line.strip():    # checks for empty lines
#             print(line_no, line)

# with open(f_path) as f:
#     line_no = 0
#     for line in f:
#         if line.strip():    # checks for empty lines
#             line_no += 1
#             print(line_no, line)

# read the file in reversed order

# with open(f_path) as f:
#     for line in reversed(list(f)):
#         print(line)

# extracting ip addresses

path = r"C:\Users\Vidya\PycharmProjects\Python_\files\access-log.txt"

with open(path) as f:
    ip_address = []
    for line in f:
        if line.strip():
            a = line.split()
            ip_address.append(a[0])
    # print(ip_address)

count_ = Counter(ip_address)
# print(count_.most_common(3))
# print(count_)
# print(set(ip_address))

############################################################################
s_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample.txt"

with open(s_path) as f:
    count = 0
    for line in f:
        if line.strip():
            count += line.count(" ")
    # print(count)

with open(s_path) as f:
    count = 0
    for line in f:
        if line.strip():
            for ch in line:
                if ch == " ":
                    count += 1
    # print(count)

with open(s_path) as f:
    d = Counter()
    for line in f:
        if line.strip():
            d += Counter(line)

    # print(d[" "])

f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\football.txt"

with open(f_path, encoding="UTF-8") as f:
    for line in f:
        if line.strip():
            a = line.split("\t")
            # print(a[1])

f_path = r"C:\Users\Vidya\PycharmProjects\Python_\files\sample2.txt"

# word = "python"
# with open(f_path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if word in line:
#             print(line_no, line)


# count = 0
# with open(f_path) as file:
#     for line in file:
#         count += 1
#         if count <= 3:
#             print(line)

# read random line
import itertools

def random_line(file_path, line_no):
    with open(file_path) as file:
        res = itertools.islice(file, line_no-1, line_no)
        print(list(res))

# random_line(f_path, 5)

# read last 2 lines

def last_2_lines(filepath):
    with open(filepath) as file:
        lines = 0
        for _ in file:
            lines += 1      # 7
        file.seek(0)
        res = itertools.islice(file, lines-2, lines)
        print(list(res))

# last_2_lines(f_path)

from collections import deque
def last_n_lines(filepath, n):
    with open(filepath) as file:
        res = deque(file, n)
        print(list(res))

last_n_lines(f_path, 2)




























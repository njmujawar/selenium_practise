"""
*
* *
* * *
* * * *
"""

# for row in range(4):
#     for col in range(row+1):
#         print("* ", end="")
#     print()

for i in range(1, 5):
    print("*")

    print("* " * i)


"""
* * * *
* * *
* *
*
"""

# for i in range(5, 0, -1):
#     print("* " * i)


"""
      *
    * *
  * * *
* * * *

"""

# for i in range(1, 5):
#     print(f'{"* " * i:>10}')

"""
    *
   * *
  * * *
 * * * *
"""

# for i in range(1, 5):
#     print(f'{"* " * i:^10}')

"""
1
1 2
1 2 3
1 2 3 4

"""
# pat = ""
# for i in range(1, 5):
#     pat += str(i) + " "     # "1", "12", "123", "1234"
#     print(f'{pat:>10}')

"""
a
a b
a b c
a b c d
a b c d e
"""

for i in range(4, -1, -1):
    for j in range(i+1):
        x = ord("a") + j
        print(chr(x), end=" ")
    print()

"""
*
*
*
* *
*
* * *
*
* * * *
"""











a = 10

print("before function call: ", a)


def spam():
    global a
    a += 10
    print("in function: ", a)


spam()

print("after function call: ", a)

####################################################################
# def spam():
#     a = 20
#
#     def nested():
#         nonlocal a
#         a += 100
#         print(a)
#
#     nested()
#
#     print(a)
# spam()















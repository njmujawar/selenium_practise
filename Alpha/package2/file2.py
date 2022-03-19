from package1.file1 import a, b

print("file2 name: ", __name__)


def multiply(n1, n2):
    print("multiplying n1 and n2....")
    print(n1 * n2)


multiply(a, b)

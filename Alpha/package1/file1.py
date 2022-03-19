a = 10
b = 20

print("file1 name: ", __name__)


def add(n1, n2):
    print("In addition function")
    print(n1 + n2)


if __name__ == "__main__":
    add(a, b)

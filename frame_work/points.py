import tracemalloc

def memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        data = func(*args, **kwargs)
        print(tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return data
    return wrapper

def make_dict(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def make_tuple(x, y, z):
    return (x, y, z)

class Points:
    __slots__ = ("x", "y", "z")     # it will not create instance dictionary
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

@memory
def read_data():
    data = [ ]
    with open('points.txt', 'r') as f:
        
        for line in f:
            parts = line.split()
            f_parts = list(map(float, parts))
            data.append(Points(f_parts[0], f_parts[1], f_parts[2]))
    return data

# Average of x, y and z co-ordinates
# a = (1.2, 1.2, 3.3)

data = read_data()
x_total = y_total = z_total = 0

for item in data:
    x_total += item.x
    y_total += item.y
    z_total += item.z

average = (x_total/len(data), y_total/len(data), z_total/len(data))

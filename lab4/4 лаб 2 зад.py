from labs import my_module


def func1(x, y):
    return my_module.my_sum(x, y)

def func2(x, y):
    return my_module.my_diff(x, y)

def func3(x, y, z):
    return my_module.my_sa(x, y, z)

print(func1(5, 6))
print(func2(40, 21))
print(func3(3, 5, 4))
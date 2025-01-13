def max_of_two(x, y):
    maxvalue = max(x, y)
    return f'максимальное число {maxvalue}'
try:
    a, b=int(input()), int(input())
    print(max_of_two(a, b))
except ValueError:
    print('Введите символ типа int')
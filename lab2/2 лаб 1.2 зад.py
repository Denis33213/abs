def square(x):
    sq=x**2
    return sq
try:
    num1=int(input('Число: '))
    print(square(num1))
except ValueError:
    print('Вводить можно только число')
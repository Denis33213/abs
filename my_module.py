def my_sum(x, y):
    return x+y

def my_diff(x, y):
    return x-y

def my_sa(*args):
    n=len(args)
    summa=sum(abs(i) for i in args)
    return summa/n

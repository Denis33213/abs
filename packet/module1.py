def check(x):
    if x:
        return True
    else:
        return False

def search(x):
    dig=[]
    if type(x)==int:
        return 'Строка состоит из цифр'
    elif type(x)==str:
        for i in x:
            if i.isdigit()==True:
                dig.append(i)
    return ''.join(dig)

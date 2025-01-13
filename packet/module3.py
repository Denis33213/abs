def is_prime(number):
    if number%2==0:
         return False
    elif number==2:
        return True
    elif number<2:
        return False
    for i in range(3, int(number**0.5)+1, 2):
        if number%i==0:
            return False
    return True


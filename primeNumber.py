from math import sqrt

def prime_search(n):
    for i in range(2, int(sqrt(n))):  #1
        if n % i == 0:                #2
            return False              #3
    return True                       #4

numero = int(input("integer number: "))
if prime_search(numero):
    print("Prime")
else:
    print("Not prime")
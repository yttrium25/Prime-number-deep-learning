import math
from sympy import sieve

def prime_list(n):
    item = []
    for i in sieve.primerange(1, n):
        item.append(i)
    return item


print(prime_list(2**30))
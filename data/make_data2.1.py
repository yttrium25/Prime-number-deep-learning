import random
import math
from sympy import sieve

def prime_list(n):
    item = []
    for i in sieve.primerange(1, n):
        item.append(i)
    return item

def Hexadecimal(i):
    item = []
    while i > 0:
        item.append(i%16)
        i //= 16

    while len(item) < 16:
        item.append(0)

    item.reverse()
    return item

def makedata(n, r): #n:データの個数 r:データの範囲
    item = []   
    plst = prime_list(int(math.sqrt(r)) + 1 )    # 素数表の作製
    for _ in range(n):
        i = random.randrange(1, r + 1)
        item.append(i)
    
    data_1 = []
    for i in item:
        i = Hexadecimal(i)
        data_1.append(i)

    data_2 = []
    for i in item:
        for p in plst:
            if i == p:
                data_2.append([1, 0])
                break
            elif i % p == 0:
                data_2.append([0, 1])  # 素数で割りきれたら０を返す
                break
        else:
            data_2.append([1, 0])
    
    return item, data_1, data_2
            
print(makedata(10, 2**10))



import random
import math
import sys
import numpy as np
from sympy import sieve

def prime_list(n):
    item = []
    for i in sieve.primerange(1, n):
        item.append(i)
    return item

def Hexadecimal(i):
    item = []
    while i > 0:
        item.append(i%2)
        i //= 2

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
    
    '''
    data_1 = []
    for i in item:
        i = Hexadecimal(i)
        data_1.append(i)
    '''
    data_0 = []
    data_1 = []
    data_2 = []
    count = 0
    count_1 = 0
    count_2 = 0
    for i in item:
        for p in plst:
            if i == p:
                data_0.append(i)
                j = Hexadecimal(i)
                data_1.append(j)
                data_2.append([1, 0])
                count =  count + 1
                count_1 =  count_1 + 1
                break
            elif i % p == 0:
                if np.random.rand() < 0.1:
                    data_0.append(i)
                    j = Hexadecimal(i)
                    data_1.append(j)
                    data_2.append([0, 1])  # 素数で割りきれたら０を返す
                    count =  count + 1
                    count_2 = count_2 + 1
                break
        else:
            data_0.append(i)
            j = Hexadecimal(i)
            data_1.append(j)
            data_2.append([1, 0])
            count =  count + 1
            count_1 = count_1 + 1 
        if count == 1000:
            print(count_1, count_2)
            break

    return data_0, data_1, data_2
            

data_0, data_1, data_2 = makedata(50000, 2**16)
data_0 = np.array(data_0)
data_1 = np.array(data_1)
data_2 = np.array(data_2)


f = open('train.py','w')

f.write('data_0 = [')
l_0 = len(data_0)
for i in range(l_0):
    item = data_0[i]
    if i < l_0 - 1:
        f.write(str(item) + ', ' )
    elif i == l_0 - 1:
        f.write(str(item))
f.write(']')

f.write('\n')

f.write('data_1 = [')
l_1 = len(data_1)   # データの個数
for i in range(l_1):
    item = data_1[i]
    ll_1 = len(item) # 配列の長さ
    if i < l_1 - 1:
        f.write('[')
        for j in range(ll_1):
            if j < ll_1 - 1:
                f.write(str(item[j]) + ", ")
            elif j == ll_1 - 1:
                f.write(str(item[j]))
                f.write('], ')
    elif i == l_1 - 1:
        f.write('[')
        for j in range(ll_1):
            if j < ll_1 - 1:
                f.write(str(item[j]) + ", ")
            elif j == ll_1 - 1:
                f.write(str(item[j]))
                f.write(']')
f.write(']')

f.write('\n')

f.write('data_2 = [')
l_2 = len(data_2)
for i in range(l_2):
    item = data_2[i]
    if i < l_2 - 1:
        f.write('[' + str(item[0]) + ', ' + str(item[1]) + '], ')
    elif i == l_2 - 1:
        f.write('[' + str(item[0]) + ', ' + str(item[1]) + ']')
f.write(']')
f.write('\n')
f.close()


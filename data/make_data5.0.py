import random
import math
import sys
import numpy as np
from sympy import sieve


def prime_list(r):  # 素数表の作成
    item = []
    for i in sieve.primerange(1, r):
        item.append(i)
    return item

def composite_list(r, x): # xの倍数を取り除いた, 合成数の表の作成
    item = []
    if x == 0:
        for i in range(r):
            item.append(i)
    else: 
        for i in range(r):
            if i % x != 0:
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


def makedata(n, r, x):  # n: データの個数, r:データの範囲, x: 取り除く倍数の指定
    data_0 = []
    data_1 = []
    data_2 = []
    plist = prime_list(r)    # 素数表
    clist = composite_list(r, x)    # xの倍数を取り除いた, 合成数の表    

    for _ in range(int(n/2)):
        p = plist[random.randint(0, len(plist) - 1)]    # 素数表の中からランダムな素数pを選び取る
        data_0.append(p)
        data_1.append(Hexadecimal(p))
        data_2.append([1, 0])
    
    for _ in range(int(n/2)):
        c = clist[random.randint(0, len(clist) - 1)]    # xの倍数を除いた数の表の中から, ランダムな要素cを選び取る
        while c in plist:   # cが素数であった場合はc  
            c = clist[random.randint(0, len(clist) - 1)]
        data_0.append(c)
        data_1.append(Hexadecimal(c))
        data_2.append([0, 1])

        '''
        for p in plist:
            if c % p == 0:
                data_0.append(c)
                data_1.append(Hexadecimal(c))
                data_2.append([0, 1])
                break
            else:
                c = clist[random.randint(1, len(clist))]
        '''
    return data_0, data_1, data_2



def write_data(name, data_0, data_1, data_2):      # 作成したデータを書き込む関数
    f = open(name, 'w')
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


data_0, data_1, data_2 = makedata(1000, 2**14, 2)
data_0 = np.array(data_0)
data_1 = np.array(data_1)
data_2 = np.array(data_2)
write_data('train.py', data_0, data_1, data_2)


data_0, data_1, data_2 = makedata(1000, 2**14, 2)
data_0 = np.array(data_0)
data_1 = np.array(data_1)
data_2 = np.array(data_2)
write_data('test.py', data_0, data_1, data_2)
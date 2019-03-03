import random
import math
import sys
import numpy as np
np.set_printoptions(threshold=np.inf)   # データ書き込みの際にデータを省略しない
from sympy import sieve
from pprint import pprint

# 素数表の作成
def prime_list(r):  
    item = []
    for i in sieve.primerange(1, r):
        item.append(i)
    return item

# xの倍数を取り除いた, 合成数の表の作成
def composite_list(r, x): 
    item = []
    if x == 0:
        for i in range(r):
            item.append(i)
    else: 
        for i in range(r):
            if i % x != 0:
                item.append(i)
    return item

# 2進数への変換の関数
def Hexadecimal(i):
    item = []
    while i > 0:
        item.append(i%2)
        i //= 2

    while len(item) < 16:
        item.append(0)

    item.reverse()
    return item

# データ作成の関数
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

    return data_0, data_1, data_2


if __name__ == '__main__':
    # トレーニングデータの作成
    data_0, data_1, data_2 = makedata(1000, 2**14, 0)
    data_0 = np.array(data_0)
    data_1 = np.array(data_1)
    data_2 = np.array(data_2)


    # トレーニングデータの書き込み
    with open("train.py", "w") as f:
        f.write('import numpy as np')
        f.write('\n')
        f.write('data_0 = np.')
        pprint(data_0, stream=f)
        f.write('data_1 = np.')
        pprint(data_1, stream=f)
        f.write('data_2 = np.')
        pprint(data_2, stream=f)

    # テストデータの作成
    data_0, data_1, data_2 = makedata(1000, 2**14, 0)
    data_0 = np.array(data_0)
    data_1 = np.array(data_1)
    data_2 = np.array(data_2)

    # テストデータの書き込み
    with open("test.py", "w") as f:
        f.write('import numpy as np')
        f.write('\n')
        f.write('data_0 = np.')
        pprint(data_0, stream=f)
        f.write('data_1 = np.')
        pprint(data_1, stream=f)
        f.write('data_2 = np.')
        pprint(data_2, stream=f)



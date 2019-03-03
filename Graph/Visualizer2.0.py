import numpy as np
import matplotlib.pyplot as plt

# ニューラルネットワークの学習をグラフィカルに表示するプログラム

N_1 = 2
N_2 = 3
N_3 = 2

W_1 = [[1, 2, 3],[ 4, 5, 6]]
W_2 = [[1, 2], [3, 4], [5, 6]]


'''
Ipt = [[1, 2], [1, 4]]          # 入力層
Hdn = [[2, 1], [2, 3], [2, 5]]  # 隠れ層
Opt = [[3, 2], [3, 4]]          # 出力層
'''

Ipt = []
Hdn = []
Opt = []

for i in range(1, N_1 + 1):
        Ipt.append([1, i / (N_1 + 1)])

for i in range(1, N_2 + 1):
        Hdn.append([2, i / (N_2 + 1)])
        
for i in range(1, N_3 + 1):
        Opt.append([3, i / (N_3 + 1)])
        


def heat_map(w):
        [w/6, 0, 1 - w/6]

def line(p, q, W, i, j):
        a, b = p[i][0], p[i][1]
        c, d = q[j][0], q[j][1]
        X = np.linspace(a, c)
        y = (d-b) * (X - a) / (c - a) + b
        w = W[i][j]
        col = [w/6, 0, 1 - w/6]
        # plt.plot(X, y, color = col, lw = W[i][j])
        plt.plot(X, y, color = col, lw = 5)



for i in range(0, N_1):
    for j in range(0, N_2):
        line(Ipt, Hdn, W_1, i, j)

for i in range(0, N_2):
    for j in range(0, N_3):
        line(Hdn, Opt, W_2, i, j)



plt.show()




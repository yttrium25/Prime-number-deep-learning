import numpy as np

import matplotlib
matplotlib.use('Agg')   # グラフ画像の保存に必要
import matplotlib.pyplot as plt

from twolayernet import TwoLayerNet

# ネットワークモデルの描画

        
def trapeziod(w, a, b, c, d):   # 台形関数
        if a <= w and w < b:
                return (w - a) / (b - a)
        elif b <= w and w <= c:
                return 1
        elif c < w and w <= d:
                return 1 - (w - c) / (d - c)
        else:
                return 0

def heatmap(X):
        Y_1 = trapeziod(X, 1/2, 3/4, 1, 5/4)
        Y_2 = trapeziod(X, 0, 1/4, 3/4, 1)
        Y_3 = trapeziod(X, -1/4, 0, 1/4, 1/2)
        return [Y_1, Y_2, Y_3]


def line(p, q, W, i, j):
        a, b = p[i][0], p[i][1]
        c, d = q[j][0], q[j][1]
        X = np.linspace(a, c)
        y = (d-b) * (X - a) / (c - a) + b
        w = abs(W[i][j])

        col = heatmap(w)
        # plt.plot(X, y, color = col, lw = W[i][j])
        plt.plot(X, y, color = col, lw = w)


def visualizer(W_1, W_2):
    
    N_1 = 16
    N_2 = 5
    N_3 = 2
    W_1 = network.params['W1']
    W_2 = network.params['W2']

    Ipt = []
    Hdn = []
    Opt = []

    for i in range(1, N_1 + 1):
            Ipt.append([1, i / (N_1 + 1)])

    for i in range(1, N_2 + 1):
            Hdn.append([2, i / (N_2 + 1)])
            
    for i in range(1, N_3 + 1):
            Opt.append([3, i / (N_3 + 1)])


    for i in range(0, N_1):
        for j in range(0, N_2):
            line(Ipt, Hdn, W_1, i, j)

    for i in range(0, N_2):
        for j in range(0, N_3):
            line(Hdn, Opt, W_2, i, j)
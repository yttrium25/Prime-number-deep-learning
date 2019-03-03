import numpy as np
import matplotlib.pyplot as plt

# ニューラルネットワークの学習をグラフィカルに表示するプログラム

input_size = 16
hidden_size = 5
output_size = 2

Ipt = [[1, 2], [1, 4]]          # 入力層
Hdn = [[2, 1], [2, 3], [2, 5]]  # 隠れ層
Opt = [[3, 2], [3, 4]]          # 出力層




def line(p, q):
    a, b = p[0], p[1]
    c, d = q[0], q[1]
    X = np.linspace(a, c)
    y = (d-b) * (X - a) / (c - a) + b
    plt.plot(X, y)
    
for p in Ipt:
    for q  in Hdn:
        line(p, q)

for q in Hdn:
    for r in Opt:
        line(q, r)



plt.show()




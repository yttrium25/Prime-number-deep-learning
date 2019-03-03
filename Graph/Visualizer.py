# 学習結果を出力, 保存する関数
import sys
sys.path.append('../')

from Result import weight 
import matplotlib.pyplot as plt
import numpy as np



def trapeziod(w, a, b, c, d):   # 台形関数
	if a <= w and w < b:
		return np.sin(np.pi * (w - a) / (2 * (b - a))) 
	elif b <= w and w <= c:
		return 1
	elif c < w and w <= d:
		return 1 - np.sin(np.pi * (w - c) / (2 * (d - c)))
	else:
		return 0

def heatmap(X):
	Red = trapeziod(X, 1/2, 3/4, 1, 5/4)
	Green = trapeziod(X, 0, 1/4, 3/4, 1)
	Blue = trapeziod(X, -1/4, 0, 1/4, 1/2)
	return [Red, Green, Blue]

def line(p, q, W, i, j):
	a, b = p[i][0], p[i][1]
	c, d = q[j][0], q[j][1]
	X = np.linspace(a, c)
	y = (d - b) * (X - a) / (c - a) + b
	w = W[i][j]


	col = heatmap(w)
	plt.plot(X, y, color = col, lw = 1)

def visualizer(W_1, W_2, b_1, b_2):
    N_1 = len(W_1)
    N_2 = len(W_2)
    N_3 = len(W_2[0])

	# ニューラルネットワーク構造の規定（座標の決定）
    Ipt = []
    Hdn = []
    Opt = []
    for i in range(1, N_1 + 1):
        Ipt.append([1, i / (N_1 + 1)])

    for i in range(1, N_2 + 1):
        Hdn.append([2, i / (N_2 + 1)])
            
    for i in range(1, N_3 + 1):
        Opt.append([3, i / (N_3 + 1)])
    

	
	# グラフ出力データの調整
    WW_1 = []
    WW_2 = []
    
	
    max_W_1 = W_1[W_1.argmax()] 
    min_W_1 = W_1[W_1.argmin()]
    print(W_1.argmax())
    print(max_W_1)
    print(min_W_1)
	# W_1の最大値を取得したい


    for w in W_1:
    	Y = []
    	for x in w:
    		y = (x - min_W_1) / (max_W_1 - min_W_1)
    		Y.append(y)
    	WW_1.append(Y)
    for w in W_2:
    	Y = []
    	for x in w:
    		y = (x - min(w)) / (max(w) - min(w))
    		Y.append(y)
    	WW_2.append(Y)
	


    # グラフの描写
    for i in range(0, N_1):
    	for j in range(0, N_2):
    		line(Ipt, Hdn, W_1, i, j)

    for i in range(0, N_2):
    	for j in range(0, N_3):
    		line(Hdn, Opt, W_2, i, j)
    
    plt.show()


if __name__ == '__main__':
	W_1 = weight.W_1
	W_2 = weight.W_2
	b_1 = weight.b_1
	b_2 = weight.b_2

	visualizer(W_1, W_2, b_1, b_2)
	





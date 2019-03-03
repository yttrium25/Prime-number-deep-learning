import numpy as np
import matplotlib.pyplot as plt



def trapeziod(w, a, b, c, d):   # 台形関数
    if a <= w and w < b:
        return (w - a) / (b - a)
    elif b <= w and w <= c:
        return 1
    elif c < w and w <= d:
        return - (w - c) / (d - c)
    else:
        return 0.0


def heatmap(X):         # ヒートマップの関数
    '''
    a, b = np.min(W), np.max(W)
    c, d = 0, 1
    w = (d - c) * (X - a) / (b - a) + c
    '''

    
    w_1 = trapeziod(X, 0, 1/6, 1/3, 1/2)
    w_2 = trapeziod(X, 1/6, 1/3, 2/3, 5/6)
    w_3 = trapeziod(X, 1/2, 2/3, 5/6, 1)
    

    # print(w_1, w_2, w_3)

    # w = W[i][j] / np.max(W)        
    return [w_1, w_2, w_3]

def main():
    
    X = np.linspace(0, 1)
    # print(X)

    # for i in range(0, 100):
    #    X = float(i/100) 
    w = [0,0,0] # heatmap(X)

    #    print(X, w[0], w[1], w[2])




    for i in range(9): 
        col = heatmap(i/10)
        Z = np.linspace(i/10, (i+1)/10)   
        plt.plot(Z, Z, color=col)  # heatmap に書き換え
        # plt.plot(X, w[1], color=heatmap(X))
        # plt.plot(X, w[2], color=heatmap(X))
    plt.show()
        



if __name__ == "__main__":
    main()
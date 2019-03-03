import numpy as np
import matplotlib.pyplot as plt



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
    '''
    if 0 <= X and X < 1/4:
        return [Y_1, Y_2, Y_3]
    elif 1/4 <= X and X <= 3/4:
        return [Y_1, Y_2, Y_3]
    elif 3/4 < X and X <= 1:
        return [Y_1, Y_2, Y_3]
    '''
    return [Y_1, Y_2, Y_3]

def main():
    '''
    for X in np.linspace(0, 1):   # Xの定義域[0, 1]
        Y = X   # X = Y の関数
        print(heatmap(X))
        plt.plot(X, Y, color=heatmap(X)) 
    plt.show()
    '''

    for i in range(10): 
        col = heatmap(i/10)
        Z = np.linspace(i/10, (i+1)/10)   
        plt.plot(Z, Z, color=col)  # heatmap に書き換え
        # plt.plot(X, w[1], color=heatmap(X))
        # plt.plot(X, w[2], color=heatmap(X))
    plt.show()


main()


'''
if __name__ == "__main__":
    main()
'''







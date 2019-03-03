import sys, os
sys.path.append(os.pardir)
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)
from data import train
from data import test
from twolayernet import TwoLayerNet

from Graph import Visualizer as vis

x_train = np.array(train.data_1)
t_train = np.array(train.data_2)
x_test = np.array(test.data_1)
t_test = np.array(test.data_2)

network = TwoLayerNet(input_size=16, hidden_size=5, output_size=2)

iters_num = 1000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    grad = network.gradient(x_batch, t_batch)

    for key in ('W1', 'b1', 'W2', 'b2'):
        network.params[key] -= learning_rate * grad[key]

    loss = network.loss(x_batch, t_batch)
    train_loss_list.append(loss)

    if i % iter_per_epoch == 0:
        train_acc = network.accuracy(x_train, t_train)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print("train acc, test acc | " + str(train_acc) + ", " + str(test_acc))



# グラフの描画
markers = {'train': 'o', 'test': 's'}
x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc', linestyle='--')
plt.xlabel("epochs")
plt.ylabel("accuracy")
plt.ylim(0, 1.0)
plt.legend(loc='lower right')
plt.show()


#

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
        

def line(p, q, W, i, j):
        a, b = p[i][0], p[i][1]
        c, d = q[j][0], q[j][1]
        X = np.linspace(a, c)
        y = (d-b) * (X - a) / (c - a) + b
        w = abs(W[i][j])
        if w > 1:
            w = 1
        col = [w, 0, 1 - w]
        # plt.plot(X, y, color = col, lw = W[i][j])
        plt.plot(X, y, color = col, lw = 1)


for i in range(0, N_1):
    for j in range(0, N_2):
        line(Ipt, Hdn, W_1, i, j)

for i in range(0, N_2):
    for j in range(0, N_3):
        line(Hdn, Opt, W_2, i, j)



plt.show()

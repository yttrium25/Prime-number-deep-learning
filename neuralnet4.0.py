import sys, os
sys.path.append(os.pardir)
import numpy as np
np.set_printoptions(threshold=np.inf)
from pprint import pprint
import matplotlib
matplotlib.use('tkagg')   # グラフ画像の保存に必要
import matplotlib.pyplot as plt



from data import train
from data import test
from twolayernet import TwoLayerNet
from Graph import Visualizer 

x_train = np.array(train.data_1)
t_train = np.array(train.data_2)
x_test = np.array(test.data_1)
t_test = np.array(test.data_2)

network = TwoLayerNet(input_size=16, hidden_size=10, output_size=2)

train_size = x_train.shape[0]
batch_size = 100     
epoch_num = 100
iters_num = epoch_num * int(max(train_size / batch_size, 1))
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

plt.savefig('Result/Graph_fig')

plt.figure()

# ネットワークモデルの描画

N_1 = 16
N_2 = 5
N_3 = 2
W_1 = network.params['W1']
W_2 = network.params['W2']
b_1 = network.params['b1']
b_2 = network.params['b2']

Visualizer.visualizer(W_1, W_2, b_1, b_2)

plt.savefig('Result/NNW_fig')

# 学習結果の保存

# 重みとバイアス
with open("Result/weight.py", "w") as f:
    f.write('import numpy as np')
    f.write('\n')
    f.write('W_1 = np.')
    pprint(W_1, stream=f)
    f.write('b_1 = np.')
    pprint(b_1, stream=f)
    f.write('W_2 = np.')
    pprint(W_2, stream=f)
    f.write('b_2 = np.')
    pprint(b_2, stream=f)


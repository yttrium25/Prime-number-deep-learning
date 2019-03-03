import sys, os
sys.path.append(os.pardir)
import numpy as np
np.set_printoptions(threshold=np.inf)
from dataset.mnist import load_mnist
from twolayernet import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
'''
    x_train = 784*60000配列（60000個の画像データ）：訓練用
    t_train = 10*60000配列（60000個の回答データ） ：訓練用
    x_test = 784*10000配列（10000個の画像データ） ：確認用
    t_test = 10*10000配列（10000個の回答データ）  ：確認用
'''

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

iters_num = 10000      # 勾配法を行う回数（学習回数）
train_size = x_train.shape[0]   # 60000個のデータ
batch_size = 100                
learning_rate = 0.1

train_loss_list = []
train_acc_list = []
test_acc_list = []

iter_per_epoch = max(train_size / batch_size, 1)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)   # 
    x_batch = x_train[batch_mask]   # 60000個のトレーニングデータの中からランダムに100個取り出した784*100配列
    t_batch = t_train[batch_mask]   # 上記100個のトレーニングデータについて、各データの答えとなる10*100配列

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
        print(train_acc, test_acc)




import sys, os
sys.path.append(os.pardir)
import numpy as np
np.set_printoptions(threshold=np.inf)
from data import sample3
#from data import sample2
from twolayernet import TwoLayerNet

x_train = np.array(sample3.data_1)
t_train = np.array(sample3.data_2)
x_test = np.array(sample3.data_1)
t_test = np.array(sample3.data_2)


network = TwoLayerNet(input_size=16, hidden_size=5, output_size=2)

iters_num = 10
train_size = 10
batch_size = 10
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
        print(train_acc, test_acc)




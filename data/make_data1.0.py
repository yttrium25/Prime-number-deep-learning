import random
from Hexadecimal import f_1
from Eratosthenes import eratosthenes

item = []
for n in range(10):
    i = random.randrange(2**10)
    item.append(i)
print(item)

data_1 = []
for i in item:
    d_1 = f_1(i)
    data_1.append(d_1)
print(data_1)

data_2 = []
for i in item:
    d_2 = eratosthenes(i)
    data_2.append(d_2)
print(data_2)



import sys

# 任意の数を16進数表記した場合の配列を与えるプログラム



# 数値を16進数に変換
def f_1(i):
    lst = []
    while i > 0:
        lst.append(i%16)
        i //= 16

    while len(lst) < 16:
        lst.append(0)

    lst.reverse()
    return lst


i = 324657
l = f_1(i)
print(l, len(l))






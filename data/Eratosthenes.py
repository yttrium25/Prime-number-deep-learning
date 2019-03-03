import math

def eratosthenes(n):
    A = [i for i in range(2, n+1)]
    P = [] # √n以下の素数リスト

    while True:
        prime = min(A)

        if prime > math.sqrt(n): # √n 以上の約数は省略
            break
        
        P.append(prime)

        i = 0
        while i < len(A):
            if A[i] % prime == 0: # Aのi番目の要素がprimeで割り切れるか判定
                A.pop(i) # Aのi番目の要素を削除
                continue
            i += 1
    
    for a in A:
        P.append(a) 

    
    for p in P:
        if n % p == 0 and p <= math.sqrt(n):
            print("{0}は{1}で割り切れる".format(n, p))
            break
    else:
        print("{0}は素数".format(n))


eratosthenes(2**10 - 1)
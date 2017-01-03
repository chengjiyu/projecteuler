"""如果一个数字将 1 到 n 的每个数字都使用且只使用了一次，我们将其称其为一个 n 位的 pandigital 数。
例如，2143 是一个 4 位的 pandigital 数，并且是一个质数。
最大的 n 位 pandigital 质数是多少？
"""
from time import time
from itertools import permutations as per

start = time()
def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1)):
            if n % i == 0:
                return False
                break
        return True
def getpan(n):
    pan = per([i for i in range(n,0,-1)],n)
    panlist = []
    for i in pan:
        k = 0
        for j in i:
            k = k*10 + j
        panlist.append(k)
    return panlist

for i in range(7,1,-1):
    num = getpan(i)
    for j in num:
        if isPrime(j):
            print(j)
            break

# for i in range(7654321, 1, -1):
#     if isPrime(i):
#         n = set(str(i))
#         if  '0' not in n and '8' not in n and '9' not in n and len(n) == len(str(i)):
#             print(i)
#             break
end = time()
print("Time : %f s" %(end-start))


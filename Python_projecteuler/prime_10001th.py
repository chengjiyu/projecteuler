"""题目：

前六个质数是 2, 3, 5, 7, 11 和 13，其中第 6 个是 13.

第 10001 个质数是多少？

要求：定义一个函数prime(n)，n为第n个质数
"""
from time import time

start = time()
def isPrime(m):
    if m == 2 or m == 3:
        return True
    elif m == 1 or m % 2 == 0:
        return False
    else:
        for i in range(3, int(m**0.5+1),2):
            if m % i == 0:
                return False
                break
        return True

a = []
def prime(n):
    for i in range(1, 200000):
        k = i
        if isPrime(i):
            a.append(i)
            if n == len(a):
                print('第10001个质数是 %d' %k)
                break

prime(10001)
end = time()
print('time : %f s' %(end-start))
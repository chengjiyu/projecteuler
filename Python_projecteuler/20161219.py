from time import time
from itertools import permutations as per
start = time()
# 判断质数， 学习'jerryxjr1220'
primes = [True]*1000000
primes[0], primes[1] = False, False
for i, isPrime in enumerate(primes):
    if isPrime:
        for j in range(i *i, 1000000, i):
            primes[j] = False
# 生成前 n 个质数和小于 100 万的所有质数
prime = []
s = 0
for i, isPrime in enumerate(primes):
    if isPrime:
        if i > 50000 and len(str(i))-1 > len(set(str(i))):
            prime.append(i)
print(prime)
def place(l):
    r = per([1, 1, 1] + [0] * (l - 4))
    return r
def replace(n):

for i in prime:
    if str(i).count('0') >= 3 or str(i).count('1') >= 3 or str(i).count('2') >= 3:
        p = place(len(str(i)))
        for j in p:
            for k in range(len(j))
                if j[k] == 1:
                    str(i)

print(time()-start)
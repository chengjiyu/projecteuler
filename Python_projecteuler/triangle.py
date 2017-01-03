"""如果 p 是一个直角三角形的周长，三角形的三边长 {a, b, c} 都是整数。对于 p = 120 一共有三组解：

{20,48,52}, {24,45,51}, {30,40,50}

对于 1000 以下的 p 中，哪一个能够产生最多的解？"""
from time import time

start = time()
count = [0]*1001
for a in range(1, 239):
    for b in range(a, 499-a):
        c = (a**2 + b**2)**0.5
        if int(c) == c and (a+b+c)<1001:
            p = int(a+b+c)
            count[p] += 1

print(count.index(max(count)))
print(time() - start)

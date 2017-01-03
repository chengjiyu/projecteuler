from time import time
from math import factorial as fac

start = time()
# 计算 C（n, r）的值
def f(n, r):
    return fac(n)/fac(r)/fac(n-r)
count = 0
# 对所有情况遍历， 判断是否大于 100 万
for n in range(23, 101):
    for r in range(1, n):
        if f(n, r) > 1000000:
            count += 1
print(count)
print(time()-start)
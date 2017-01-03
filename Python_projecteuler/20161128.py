#coding:utf-8
import time
start = time.time()
primes = [True]*200000
primes[0],primes[1] = False,False
# 质数
for i,prime in enumerate(primes):
    if prime:
        for j in range(i*i,200000,i):
            primes[j] = False
plist = []
for i,prime in enumerate(primes):
    if prime:
        plist.append(i)
pdic = {}
for i in range(2,200000):
    if primes[i]:
        pdic[i] = [i]
        flag = 0
    else:
        t = i
        for p in plist:
            if t%p == 0:
                t //= p
                pdic[i] = pdic[t] + [p]
                c = len(set(pdic[i]))
                break
        if c >= 4:
            flag += 1
        else:
            flag = 0
        if flag >= 4:
            print ('找到最小的具有4个不同因子的4个连续整数，其中最小的是%d' % (i-3))
            break
print ('用时: %.3f 秒' % (time.time()-start))
print ('用时: %.3f 秒' % (time.time()-start))
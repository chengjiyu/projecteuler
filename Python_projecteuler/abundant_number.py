"""题目：

如果一个数的所有真因子之和等于这个数，那么这个数被称为完全数。例如，28 的所有真因子之和为 1 + 2 + 4 + 7 + 14 = 28，所以 28 是一个完全数。

如果一个数的所有真因子之和小于这个数，称其为不足数，如果大于这个数，称其为过剩数。

12 是最小的过剩数，1 + 2 + 3 + 4 + 6 = 16。因此最小的能够写成两个过剩数之和的数字是 24。经过分析，可以证明所有大于 28123 的数字都可以被写成两个过剩数之和。但是这个上界并不能被进一步缩小，即使我们知道最大的不能表示为两个过剩数之和的数字要比这个上界小。

找出所有不能表示为两个过剩数之和的正整数之和。
"""
from time import time
start = time()
def d(n):
    # 是否过剩数
    result = set()
    for i in range(2,int(n**.5)+1):
        if not n % i:
            result.update({i, n // i})
    return n > 1 and sum(result) + 1 > n

limite = range(20613)
abdn = []
result = [i for i in limite]
for i in limite:
    if d(i):
        abdn.append(i)
        for e in abdn:
            temp =  i+e
            if temp > 20612:
                break
            result[temp] = 0

print(sum(result))

end = time()
print('Time : %f s' %(end-start))
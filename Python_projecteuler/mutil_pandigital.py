"""如果一个 n 位数使用了 1 到 n 中每个数字且只使用了一次，我们称其为 pandigital。例如，15234 这个五位数，是 1 到 5 pandigital 的。

7254 是一个不寻常的数，因为：39 × 186 = 7254 这个算式的乘数，被乘数和乘积组成了一个1到 9 的 pandigital 组合。

 找出所有能够组合成 1 到 9 pandigital 的乘法算式中乘积的和。

 提示: 有的乘积数字能够被多个乘法算式得到，所以在计算时要记得只计算它们一次。

"""
from time import time
start = time()

b = set()
for i in range(1,100):
    for j in range(1000//i,10000//i):
        n = i * j
        p = str(i)+str(j)+str(n)
        if len(p) == 9:
            p = set(p)
            if len(p) == 9 and '0'not in p:
                b.add(n)
end = time()
print(sum(b))
print("Time : %f s" %(end-start))
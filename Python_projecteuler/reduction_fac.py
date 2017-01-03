"""题目：

分数 49/98 是一个奇怪的分数：当一个菜鸟数学家试图对其进行简化时，他可能会错误地可以认为通过将分子和分母上的

9 同时去除得到 49/98 = 4/8。但他得到的结果却是正确的。

我们将 30/50 = 3/5 这样的分数作为普通个例。

一共有四个这样的非普通分数，其值小于 1，并且包括分子和分母都包括 2 位数。

如果将这四个分数的乘积约分到最简式，分母是多少？
"""
from fractions import Fraction
from time import time
start = time()
product = 1
for i1 in range(1, 10):
    for i2 in range(1, 10):
        for j in range(1, 10):
            frac = Fraction(i1 * 10 + i2, i2 * 10 + j)
            if frac < 1 and frac == Fraction(i1, j):
                product *= frac
                print(frac)
print(product.denominator)
end = time()
print("Time : %f s" %(end-start))
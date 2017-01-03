"""145 是一个奇怪的数字, 因为 1! + 4! + 5! = 1 + 24 + 120 = 145.

找出所有等于各位数字阶乘之和的数字之和。

注意: 因为 1! = 1 和 2! = 2 不是和的形式，所以它们不算在内。
"""
import math
import  time

# 先考虑上限是多少：
# 即使每位都是9，如果是8为则9!*8=2903040，只有7位。所以不可能是8位。
# 如果是7位则9!*7=2540160，因最前一位只能最大是2，所以只能到达9！*6+2，即2177282
# start = time.clock()
#
# list1 = [math.factorial(i) for i in range(10)]
# sum2 = 0
# for i in range(10, 2177283):
#     j = i
#     sum1 = 0
#     while j > 0:
#         sum1 += list1[j%10]
#         j //= 10
#     if sum1 == i:
#         sum2 += sum1
# print(sum2)
# end = time.clock()
# print("time : %f s" %(end-start))

s = 0
dict_fac = {str(i):math.factorial(i) for i in range(10)}
get_fac = dict_fac.get
for n in range(3, 50000):
    if n == sum(map(get_fac, str(n))):
        s += n
print(s)
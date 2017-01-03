"""十进制数字585=1001001001(二进制),可以看出在十进制和二进制下都是回文（从左向右读和从右向左读都一样）。

求 100 万以下所有在十进制和二进制下都是回文的数字之和。

（注意在两种进制下的数字都不包括最前面的 0）
"""
import time
start = time.clock()

sum = 0
def shu(n):
    n = str(n)
    s1 = int(n + n[::-1])
    s2 = int(n + n[:-1][::-1])
    return s1, s2
for i in range(1, 999):
    x1, x2 = shu(i)
    # 用字符串的format算二进制，而不是用bin函数，是避免开头的0b
    # x = '{:b}'.format(x1)
    if bin(x1)[2:] == bin(x1)[2:][::-1]:
        sum += x1
    if bin(x2)[2:] == bin(x2)[2:][::-1]:
        sum += x2
print(sum)
end = time.clock()
print("time : %f s" %(end-start))
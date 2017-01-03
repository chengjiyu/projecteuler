"""将正整数连接起来可以得到一个无理小数：

0.123456789101112131415161718192021...

可以看出小数部分的第 12 位是 1。

如果用 dn表示这个数小数部分的第 n 位，找出如下表达式的值：
d1*d10*d100*d1000*d10000*d100000*d1000000

"""
import time
start = time.clock()
a = ''

for i in range(1, 100000):
    a += str(i)
m = int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])
print(m)

s = ''
i = 1
n = 1
while len(s)<1000001:
    s += str(i)
    i += 1
for j in range(1,7):
    n *= int(s[10**j-1])
print(n)
end = time.clock()
print("time : %f s" %(end-start))
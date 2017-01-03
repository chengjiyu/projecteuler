"""令人惊奇的，只有三个数能够写成它们各位数的四次方之和：
1634=1(4)+6(4)+3(4)+4(4)
8208=8(4)+2(4)+0(4)+8(4)
9474=9(4)+4(4)+7(4)+4(4)
1=1(4) 没有被算作在内因为它不是一个和。
这些数字的和是 1634 + 8208 + 9474 = 19316.
找出所有能被写成各位数字五次方之和的数，并给出这些数的和。
"""
from time import time
start = time()

sum = 0
for i in range(2, 295277):
    j = i
    power = 0
    while j:
        power += (j % 10) ** 5
        j //= 10
    if power == i:
        sum += i
print(sum)
end = time()
print("Time : %f s" %(end-start))

power_5 = {str(i):i**5 for i in range(0,10)}
result = 0
print(power_5)

for i in range(2,12):
    n = power_5.get(str(i))
    print(n)
    if  power_5.get(str(i))== i:
        result += i
        print(i)
print(result)
print("Time2 : %f s" %(time()-end))
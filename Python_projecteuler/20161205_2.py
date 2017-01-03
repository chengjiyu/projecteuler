from time import time

start = time()
# 质数判断
def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n <= 1 or n % 2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5+1),2):
            if n % i == 0:
                return False
        return True

# 生成所有4位的质数
prime = set()
for i in range(1000, 10000):
    if isPrime(i):
        prime.add(i)
        
# 如果满足1. 序列中的每个数都是质数。 2. 每个四位数都是其他数字的一种排列。
for i in prime:
    if i != 1487:
        j = i + 3330
        k = i + 6660
        if j in prime and k in prime:
            if sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
                print(str(i)+str(j)+str(k)) 
                break
     
print(time() - start)         

# 附加题
print(str(sum([x**x for x in range(1,1000)]))[-10:])


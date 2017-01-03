from time import time
import itertools

start = time()

##primes = [True]*10000
##primes[0], primes[1] = False, False
##for i, p in enumerate(primes):
##    if p:
##        for j in range(i*i, 10000, i):
##            primes[j] = False
##prime = set()
##for i, p in enumerate(primes):
##    if p:
##        prime.add(i)
##        
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
for i in range(1488, 10000):
    if isPrime(i):
        prime.add(i)


### 对质数进行排列，生成新的质数
##def per(n):
##    l_1 = []
##    while n:
##        a = n % 10
##        l_1.append(a)
##        n //= 10
##    num = itertools.permutations(l_1)
##    l_2 = []
##    for i in num:
##        x = 0
##        for j in i:
##            x = x*10 + j
##        if x in prime:
##            l_2.append(x)
##    return l_2


# 如果满足递增条件，输出结果
for i in prime:
    j = i + 3330
    k = i + 6660
    if (j) in prime and (k) in prime:
        if sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
            ans = i
            break
print(i,j,k)      
print(time() - start)         

# 附加题
print(str(sum([x**x for x in range(1,1000)]))[-10:])

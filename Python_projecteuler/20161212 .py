from time import time
start = time()
# 判断质数， 学习'jerryxjr1220'
primes = [True]*1000000
primes[0], primes[1] = False, False
for i, isPrime in enumerate(primes):
    if isPrime:
        for j in range(i *i, 1000000, i):
            primes[j] = False
# 生成前 n 个质数和小于 100 万的所有质数
prime = []
s = 0
for i, isPrime in enumerate(primes):
    if isPrime:
        s += i
        if s > 1000000:
            break
        prime.append(i)

def find():
    for length in range(len(prime)-1 , 2, -1):     # length 表示连续质数序列的长度, 从最长的开始计算
        for start in range(0, len(prime)- length +1):
            # start ：start + length 表示选择连续相加的质数范围， 要求start + length < len(prime)质数列表长度
            result = sum(prime[start:start + length])
            if primes[result]:
                print(result)
                print(length)
                return 0

if __name__ == "__main__":
    find()
    print(time()-start)


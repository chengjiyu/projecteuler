"""在英国，货币是由英镑 ￡，便士 p 构成的。一共有八种钱币在流通：

1p, 2p, 5p, 10p, 20p, 50p, ￡1 (100p) 和 ￡2 (200p).
要构造 ￡2 可以用如下方法：

1×￡1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

允许使用任意数目的钱币，一共有多少种构造 ￡2 的方法？
"""
# 思路是动态规划的思想，把整个过程分为8个阶段，即当只有1p的时候1p到200p分别只有一种凑法，
# 然后计算既有1p又有2p的时候1p到200p各有多少种凑法，然后在计算加多个5p的时候，1p到200p各有多少种凑法。。依次类推到200p
# 这里可以用递归的方法，缺点是比较慢（递归都是这通病）。理解了递归的思路后，用列表从正面求比较快。
#  算法1（递归思路）：
from time import time
on = time()
s = [0,1,2,5,10,20,50,100,200]
def f(x,y):
    if x<0 or y<=0:
        return 0
    if x==0:
        return 1
    return f(x,y-1) + f(x-s[y],y)

print(f(200,8))
print("Time : %f s" %(time()-on))
# 算法2（列表正面求解）：
start = time()
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1]+[0]*target
for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]
print(ways[target])
end = time()
print("Time : %f s" %(end-start))
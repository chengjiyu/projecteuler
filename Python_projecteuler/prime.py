"""3797 这个数很有趣。它本身是质数，而且如果我们从左边不断地裁去数字，得到的仍然都是质数：3797, 797, 97, 7。而且我们还可以从右向左裁剪：3797, 379, 37, 3，得到的仍然都是质数。

找出全部 11 个这样从左向右和从右向左都可以裁剪的质数。

注意：2, 3, 5 和 7 不被认为是可裁剪的质数。
"""
# 先说思路：一个n位的数字(根据要求知n>1),将其为为三段：首1位，中间n-2位，末1位，要满足左右截后都是质数
# 1、首1位只能是【2，3，5，7】。因为向左截到只有首位时要为质数
# 2、末位只能是【3，7】。因为向右截到只有末位时，可在【2，3，5，7】中选，但如果不截位时，末位【2，5】的不是质数，所以末位只能是【3，7】
# 3、中间n-2位只能是【1，3，7，9】。因为向左截时，中间任何一位数都可能变成末位，末位如果是偶数和5时，则不是质数。
# 4、将上述三段进行排列组合后，再进行截位质数判断。
import time
import itertools
import math
start = time.clock()
def isPrime(n):
    flag = 1
    if n == 2 or n == 3:
        return  1
    elif n % 2 == 0:
        return 0
    else:
        for i in range(3, int(n**0.5+1), 2):
            if n % i == 0:
                flag = 0
                break
        return flag
def check_all_prime(zs): # 左右裁去数字进行质数判断
    for i in range(0,len(zs)):
        if isPrime(int(zs[0:i+1])):
            if isPrime(int(zs[len(zs)-i-1:])): # zs[len(zs)-i-1:]比zs[i:]快， 数小判断质数快
                pass
            else:
                return False
        else:
            return False
    return True

list_start=[2,3,5,7] # 首位可能出现的数字
list_end=[3,7] # 末位可能出现的数字

# count记录左右截去后都为质数的数字的个数,m为除去首位和末位的中间部分的位数，并赋初值
count=0
m=0

while 1:
    if count==11: # 如果找到11个，则跳出循环
        break
    else:
        list_mid=[] # list_mid存放中间位数的列表
        for eachone in list(itertools.product(['1','3','7','9'],repeat = m)): # 生成中间位数的列表
            s=''
            for each in eachone:
                s+=each
            list_mid.append(s)

        # 通过list_start，list_mid,list_end来进行组合
        for int_start in list_start:
            for str_mid in list_mid:
                for int_end in list_end:
                    aa=str(int_start)+str_mid+str(int_end)
                    if check_all_prime(aa):
                        count+=1
                        print(aa)
        m+=1

end = time.clock()
print('time: %f s' %(end - start))
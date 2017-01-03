"""我们称 197 为一个循环质数，因为它的所有轮转形式： 197, 971 和 719 都是质数。

100 以下有 13 个这样的质数： 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 和 97.

100 万以下有多少个循环质数？

答案是55
"""
import time
import itertools
start = time.clock()
def isPrime(n):
    flag = 1
    if n == 2 or n == 3:
        return 1
    elif n % 2 == 0 or n == 1:
        return 0
    else:
        for i in range(3, int(n**0.5+1), 2):
            if n % i == 0:
                flag = 0
                break
        return flag

def check_nm(j): #是否为循环质数
    list_each=[]
    for each_str in j:
        list_each.append(each_str)
    for i in range(0,len(list_each)):
        s=''
        for each in list_each:
            s+=each
        if isPrime(int(s)):
            list_each.append(list_each[0])
            del list_each[0]
        else:
            return 0
    return 1

list_temp=['2','5']
for i in range(1, 2):
    for eachone in list(itertools.product(['1','3','7','9'],repeat = i)):
        s=''
        for aa in eachone:
            s+=aa
        if check_nm(s):
            list_temp.append(s)

print(len(list_temp))
end = time.clock()
print('time : %f s' %(end-start))
"""10 以下的质数的和是 2 + 3 + 5 + 7 = 17.

找出两百万以下所有质数的和。



我的解题思路，供参考：
方法1：sum1 = 2，从3开始步长为2（除2以外的质数都是奇数）到2000000，分别测试是否质数，如果是质数则加到sum1中，这样效率比较低，但占用空间少。
方法2：建立列表[2]，从3开始步长为2到2000000，将数字依次对列表的值取余（仅算到列表中数值小于数字的平方根），如果取余都不为0则是质数，加到列表中，最后对列表整体求和。这样效率高于方法1，但占用空间多。
方法3：建立列表，其值为1~2000000，从2开始往后的值如果是2的倍数则将其值改为0，依次进行直至到2000000的平方根，最后对列表整体求和。这样效率高于方法2，因乘法快于除法，占用的空间也多。
"""
def a(n):
    a=[1]*(n+1)
    m=2
    su=0
    while m<=n:
        if a[m]:
            su+=m
            l=2*m
            while l<=n:
                a[l]=0
                l+=m
        m+=1
    return su
print(a(2000000))
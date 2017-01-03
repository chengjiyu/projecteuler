from time import time

start = time()

set1 = set('0123456789')
num = [13, 11, 7, 5, 3, 2]
list1 = [str(i) if i >= 100 else '0'+str(i) for i in range(17,1000) if i % 17 == 0]
list1 = [i for i in list1 if len(set(i)) == 3]
for n in num:
    list2 = []
    for i in list1:
        for j in set1-set(i):
            if (int(j + i[:2]) % n) == 0:
                list2.append(j+i)
    list1 = list2[:]
list1 = [list(set1-set(i))[0]+i for i in list1]
print(list1)
sum1 = sum([int(i) for i in list1])
print(sum1)
print(time()-start)

lambda_1 = 1.0722
lambda_2 = 0.48976
sigma_1 = 8.4733*10**(-4)
sigma_2 = 5.0201*10**(-6)
a = sigma_2/(sigma_1+sigma_2)
b = sigma_1/(sigma_1+sigma_2)
c = a*lambda_2+b*lambda_1
print(a,b,0.49/c)
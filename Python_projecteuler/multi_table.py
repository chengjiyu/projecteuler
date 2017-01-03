# 乘法表
for i in range(1,int(input())+1):print(' '.join(map(lambda x:str(x[0]*x[1]),enumerate([i]*i,1))))

a=range(1,int(input())+1);list(map(lambda x:print(' '.join(map(lambda y:str(x*y),a[:x]))),a))

for i in range(1,10):
    for j in range(1, i + 1):
        if j != 0:
            print("%s * %s = %s\t" % (j, i, i * j)),
    print("\n"),
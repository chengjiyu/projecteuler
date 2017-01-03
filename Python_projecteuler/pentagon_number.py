from time import time

start = time()

f = [n*(3*n-1)/2 for n in range(1,10000)]
fi = set(f)
for j in range(len(f)):
    for k in range(j+1,len(f)):
        if (f[k]+f[j]) in fi and (f[k]-f[j]) in fi:
            D = f[k]-f[j]

print(D)

print('Time:%f' %(time()-start))
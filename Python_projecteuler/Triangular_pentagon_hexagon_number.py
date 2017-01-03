from time import time

start = time()

T = set(i*(i+1)/2 for i in range(285,100000))       # 生成三角数
P = set(j*(3*j-1)/2 for j in range(165,100000))     # 生成五角数
H = set(k*(2*k-1) for k in range(143,100000))       # 生成六角数

# for n in T:
#     if n in P and n in H:
#         print(n)

print(T&P&H)        # 取交集

grid = [[1],[0]]
print(len(grid))
l = 0
for i in grid:
    l += sum(i)
p = 4*l

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i+1 < len(grid) and grid[i][j] == grid[i+1][j] == 1:
            p -= 2
for j in range(len(grid[0])):
    for i in range(len(grid)):
        if j+1 < len(grid[0]) and grid[i][j] == grid[i][j+1] == 1:
            p -= 2
print(p)

print('Time: %f' %(time()-start))
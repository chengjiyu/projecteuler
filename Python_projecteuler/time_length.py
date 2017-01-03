list1 = [1,2,3,4,5,6,0]
list2 = [0,2,3,3,2,1,2]
c = []
queue = []      # 保存队列长度
for j in range(max(list2)+1):       # j 是队长列表中的值
    queue.append(j)
    b = [i for i, a in enumerate(list2) if a == j]      # b 是不同队长对应的索引值
    c.append(b)
wait = []
for k in range(len(c)):
    s = 0
    for l in range(len(c[k])):
        s += list1[c[k][l]]     # [c[k][l]] 是队长列表相同队长对应等待时间的索引值
    wait.append(s/len(c[k]))

print(queue,wait)
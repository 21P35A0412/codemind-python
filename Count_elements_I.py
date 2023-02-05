n,m=map(int,input().split())
a=list(set(list(map(int,input().split()))))
b=list(set(list(map(int,input().split()))))
c=[]
for i in a:
    if i in b:
        c.append(i)
for j in b:
    if j in a:
        c.append(j)
print(len(list(set((c)))))
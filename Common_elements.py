n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in a:
    if i not in d:
        d.append(i)
for j in d:
    if j in b:
        c.append(j)
print(*c)
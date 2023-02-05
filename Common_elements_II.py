n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
y=[]
for d in a:
    if d not in x:
        x.append(d)
for e in b:
    if e not in y:
        y.append(e)
c=[]
for i in x:
    if i not in y:
        c.append(i)
for j in y:
    if j not in x:
        c.append(j)
print(*c)
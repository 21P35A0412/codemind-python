n=int(input())
a=list(map(int,input().split()))
c=[]
d=[]
e=[]
s=0
for j in range(len(a)):
    if j%2==1:
        c.append(a[j])
    else:
        d.append(a[j])
for i in d:
    for k in range(c[s]):
        e.append(i)
    s+=1
print(*e)
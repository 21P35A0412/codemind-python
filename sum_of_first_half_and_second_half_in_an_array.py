t=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
n=t//2
for i in range(n):
    b.append(a[i])
for j in a:
    if j not in b:
        c.append(j)
print(sum(b))
print(sum(c))
    
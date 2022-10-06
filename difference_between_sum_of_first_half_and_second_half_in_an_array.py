N=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
t=N//2
for i in range(t):
    b.append(a[i])
for j in a:
    if j not in b:
        c.append(j)
print(abs(sum(b)-sum(c)))
    
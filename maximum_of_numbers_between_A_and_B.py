n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
s=0
for i in range(n):
    if a<=m[i]<=b:
        c.append(m[i])
        s=1
if s==1:
    print(max(c))
else:
    print(-1)
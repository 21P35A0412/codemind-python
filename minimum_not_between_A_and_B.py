n=int(input())
m=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
s=0
for i in m:
    if i<a or i>b:
        c.append(i)
        s+=1
if s==0:
    print(-1)
else:
    print(min(*c))
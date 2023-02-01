n=int(input())
b=[]
a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        b.append(i)
d=list(set(b))
print(len(d))
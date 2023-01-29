n=int(input())
a=list(map(int,input().split()))
b=list(set(a))
s=0
for i in b:
    if i%2==1 and b.count(i)==1:
        s+=1
print(s)
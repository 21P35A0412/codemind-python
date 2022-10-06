t=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i%2==0:
        s+=i
    if i%2!=0:
        break
print(s)
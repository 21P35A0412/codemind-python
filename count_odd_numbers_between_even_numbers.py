m=int(input())
a=list(map(int,input().split()))
i=0
c=0
while i<=len(a)-3:
    if a[i]%2==0 and (a[i+2]%2)==0 and a[i+1]%2==1:
        c+=1
    i+=1
print(c)
n=input()
a=list(map(int,input().split()))
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
d=set(list(b))
print(sum(d))
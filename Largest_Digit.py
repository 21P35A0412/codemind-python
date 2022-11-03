n=int(input())
i=0
while n>0:
    r=n%10
    if r>i:
        i=r
    n=n//10
print(i)
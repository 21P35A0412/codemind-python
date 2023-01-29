n=int(input())
a=list(map(int,input().split()))
if n%2==1:
    a.append(0)
print(*a)
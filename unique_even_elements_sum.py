n=int(input())
a=list(map(int,input().split()))
b=set(list(a))
y=[c for c in b if c%2==0]
print(sum(y))
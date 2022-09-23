n=int(input())
m=int(input())
s = 0
r=0
for i in range(1,n):
    if n%i==0:
        s += i
for l in range(1,m):
    if m%l==0:
        r+=l
if s==m and r==n:
    print("Amicable")
else:
    print("Not Amicable")
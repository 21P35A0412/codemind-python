n = int(input())
for i in str(n):
    r = n % 10 
    n=n//10
    print(r,end='')

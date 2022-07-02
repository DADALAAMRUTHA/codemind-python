n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in range(n):
    s=s+(2**p)*a[n-i-1]
    p=p+1
print(s)
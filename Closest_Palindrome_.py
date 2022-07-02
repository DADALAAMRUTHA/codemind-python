def palin(n):
    rev=0
    p=n
    while(n):
        r=n%10
        n=n//10
        rev=rev*10+r
    if rev==p:
        return p
n=int(input()) 
c1=0
c2=0
i=n+1
k=n-1
while True:
    c1=c1+1
    if palin(i)==i:
        z=i
        break
    i=i+1
while True:
    c2=c2+1
    if palin(k)==k:
        p=k
        break
    k=k-1
if c1==c2:
    print(p,z)
elif c1<c2:
    print(z)
else:
    print(p)
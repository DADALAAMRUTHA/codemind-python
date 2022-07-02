def prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**0.5)):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
p=1
c=0
for i in range(1,(n//2)+1):
    if n%i==0 and prime(i):
       print(i,end=" ")
       c=c+1
if c<1:
    print(-1)
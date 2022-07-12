n=int(input())
l=list(map(int,input.().split()))
a,b=map(int,input().split())
s=0
for i in range(n):
    if l[i]>=a and l[i]<=b:
        s=s+l[i}
print(s)
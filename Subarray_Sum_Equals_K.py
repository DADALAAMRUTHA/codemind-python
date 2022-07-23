n,b=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    sum=0
    for j in range(i,len(a)):
        sum=sum+a[j]
        if sum==b:
            c+=1
            break
print(c)
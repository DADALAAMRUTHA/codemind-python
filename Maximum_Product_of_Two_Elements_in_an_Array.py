l=list(map(int,input().split()))
for i in range(len(l)):
    l[i]=l[i]-1
ma=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if i!=j:
            if l[i]*l[j]>ma:
                ma=l[i]*l[j]
print(ma)
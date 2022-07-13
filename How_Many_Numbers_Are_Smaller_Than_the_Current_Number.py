n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    c=0
    for j in range(n):
        if j!=i:
            if l[j]<l[i]:
                c+=1
    a.append(c)
print(*a)
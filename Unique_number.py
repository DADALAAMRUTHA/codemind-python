n=int(input())
a=[]
p=0
for i in str(n):
    a.append(i)
for i in range(len(a)):
    c=1
    for j in range(len(a)):
        if a[i]==a[j] and i!=j:
             c=c+1
    if c==1:
        p=p+1
if p==len(a):
    print("Unique Number")
else:
    print("Not Unique Number")
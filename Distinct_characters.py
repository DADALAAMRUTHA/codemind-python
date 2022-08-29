n=input()
n=n.lower()
a=[]
b=[]
for i in range(len(n)):
    if n[i]!=' ':
        a.append(n[i])
a=list(a)
for i in a:
    c=0
    for j in range(len(a)):
        if i==a[j]:
            c+=1
    if c==1:
        b.append(i)
b=sorted(b)
for i in b:
    print(i,end='')
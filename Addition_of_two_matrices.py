n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
b=[]
for i in range(n):
    b.append(list(map(int,input().split())))
    
c=[]
for i in range(n):
    d=[]
    for j in range(n):
        d.append(a[i][j]+b[i][j])
    c.append(d)
for i in range(n):
    print(*c[i])
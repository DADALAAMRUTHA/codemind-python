x=int(input())
r=0
i=0
a=1
b=1
c=2
if x==0:
    print("1")
elif x<=2:
    print(x)
else:
    for i in range(3,x+1):
        r=a+b+c
        a=b
        b=c
        c=r
    print(r)
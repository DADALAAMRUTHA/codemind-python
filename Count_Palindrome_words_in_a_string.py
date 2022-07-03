n=input()
n1=n.lower()
s=n1.split()
c=0
for i in s:
    k=i
    p=i[::-1]
    if k==p:
        c=c+1
print(c) 
a=str(input())
b=a.split()
c=[]
d=[]
for i in range(len(b)):
    c.append(b[i])
print(*(c[::-1]))
n=input()
k='aeiouAEIOU'
d=[]
p=0
for i in n:
    if i in k and i not in d:
        d.append(i)
if len(d)>0:
    print(*d)
else:
    print(-1)
n=int(input())
arr=list(map(int,input().split()))
c=0
mi=100000000
for i in range(n):
    if len(str(arr[i]))<mi:
        mi=len(str(arr[i]))
for i in range(n):
    if len(str(arr[i]))==mi:
        c=c+1
print(c)
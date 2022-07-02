n=int(input())
arr=list(map(int,input().split()))
c=0
max=0
for i in range(n):
    if len(str(arr[i]))>max:
        max=len(str(arr[i]))
for i in range(n):
    if len(str(arr[i]))==max:
        print(arr[i],end=" ")
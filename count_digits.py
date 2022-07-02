n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    k=str(abs(a[i]))
    print(len(k),end=" ")
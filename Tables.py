n,r=map(int,input().split())
c=0
for i in range(1,r+1):
    if i%2!=0:
        c=n*i
        print('%d x %d = %d'%(n,i,c))
n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
l=[]
c=0
for i in range(n):
    if a[i]>=x and a[i]<=y:
        l.append(a[i])
        c=1
if c==0:
    print(-1)
else:
    print(*l)
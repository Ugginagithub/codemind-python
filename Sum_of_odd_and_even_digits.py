n=int(input())
arr=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es=es+arr[i]
    else:
        os=os+arr[i]
res=es-os
if(res==0):
    print('YES')
else:
    print('NO')
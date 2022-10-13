n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1,0,-1):
    if a[i]%2==0:
        print(i,end=' ')
        c+=1
        break
if c==0:
    print('0')
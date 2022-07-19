n=int(input())
arr=list(map(int,input().split()))
c=0
c1=0
for i in range(0,n):
    if(arr[i]%2!=0):
        c+=1
        if(i%2!=0):
            c1+=1
if(c==c1):
    print('True')
else:
    print('False')
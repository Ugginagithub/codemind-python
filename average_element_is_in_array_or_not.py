n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    s+=i
k=s//n
c=0
for i in arr:
    if(i==k):
        c+=1
if(c>0):
    print('True')
else:
    print('False')
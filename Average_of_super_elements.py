n=int(input())
arr=list(map(int,input().split()))
c,s=0,0
for i in set(arr):
    if(arr.count(i)==i):
        s+=i
        c+=1
if(c==0):
    print('-1')
else:
    k=s/c
    print("%.2f"%k)
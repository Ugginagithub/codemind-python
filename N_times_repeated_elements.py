n=int(input())
arr=list(map(int,input().split()))
a=int(input())
c=0
b=[]
for i in set(arr):
    if(arr.count(i)==a):
        c=1
        b.append(i)
if(c!=0):
    print(*set(b))
else:
    print('-1')
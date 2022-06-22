n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
k=[]
for i in range(len(arr)):
    if(arr[i]>=a and arr[i]<=b):
        c+=1
        k.append(arr[i])
if(c==0):
    print("-1")
else:
    print(min(k))
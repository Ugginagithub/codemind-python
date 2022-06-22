n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
g=[]
c=0
for i in range(len(arr)):
    if arr[i]>=a and arr[i]<=b:
        k.append(arr[i])
for i in range(len(arr)):
    if arr[i] not in k:
        c+=1
        g.append(arr[i])
if(c==0):
    print("-1")
else:
    print(min(g))
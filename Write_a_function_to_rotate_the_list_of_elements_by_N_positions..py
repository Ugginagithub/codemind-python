n=int(input())
arr=list(map(int,input().split()))
m=int(input())
for i in range(m):
    temp=arr[0]
    arr[0]=arr[n-1]
    for j in range(1,n):
        d=arr[j]
        arr[j]=temp
        temp=d
for i in arr:
    print(i,end=" ")
        
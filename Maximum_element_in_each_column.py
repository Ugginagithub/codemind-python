n,m=map(int,input().split())
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
for i in range(m):
    s=0
    for j in range(n):
        if s<arr[j][i]:
            s=arr[j][i]
    print(s)
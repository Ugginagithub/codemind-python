n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(n):
        if(arr[i]==arr[j] and i!=j):
            c+=1
    if(c>=n//2):
        print(arr[i])
        break
        
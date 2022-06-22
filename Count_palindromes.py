def pali(n):
    rev=0
    m=n*1
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    if(rev==m):
        return 1
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if(pali(arr[i])):
        c+=1
print(c)
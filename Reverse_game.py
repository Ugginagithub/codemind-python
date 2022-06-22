def pali(n):
    rev=0
    m=n*1
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    print(pali(i),end=' ')
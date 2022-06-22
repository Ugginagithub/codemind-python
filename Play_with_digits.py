def sum(n):
    sum=0
    while n:
        r=n%10
        sum=sum+r
        n=n//10
    return sum
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    c=c+sum(i)
print(c)
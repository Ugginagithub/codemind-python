def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input())
sum=0
k=n*1
while(n):
    r=n%10
    sum=sum+fact(r)
    n=n//10
if(sum==k):
    print('The number %d is a strong number'%k)
else:
    print('The number %d is not a strong number'%k)
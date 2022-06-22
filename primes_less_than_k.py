def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
arr=list(map(int,input().split()))
a=int(input())
c=0
for i in arr:
    if(prime(i)):
        if(i<=a):
            c+=1
print(c)
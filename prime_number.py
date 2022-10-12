def pri(n):
    if n==1:
        return 0
    for i in range(2,int(n//2)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
if pri(n):
    print("prime")
else:
    print("not a prime")
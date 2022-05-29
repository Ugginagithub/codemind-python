def pali(n):
    rev=0
    while n:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
n=int(input())
for i in range(1,n+1):
    b=int(input())
    if(b==pali(b)):
        print('True')
    else:
        print('False')
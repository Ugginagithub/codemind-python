n=int(input())
rev=0
rev1=0
if(n<0):
    m=n*(-1)
    while m:
        rev=rev*10+m%10
        m//=10
    print("-%d"%rev)
else:
    while n:
        rev1=rev1*10+n%10
        n//=10
    print("%d"%rev1)

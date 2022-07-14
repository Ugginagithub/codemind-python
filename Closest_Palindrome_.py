def pali(n):
    t=n
    rev=0
    while(n):
        rev=rev*10+n%10
        n=n//10
    if(rev==t):
        return 1
    else:
        return 0
n=int(input())
p1=0
p2=0
for i in range(n-1,1,-1):
    if(pali(i)):
        p1=i
        break
for i in range(n+1,100000000):
    if(pali(i)):
        p2=i
        break
if(n-p1==p2-n):
    print(p1,p2)
else:
    print(p1)
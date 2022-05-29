n=int(input())
l=len(str(n))
s=0
k=n*1
while n>0:
    r=n%10
    s=s+r**l
    n=n//10
    l=l-1
if(s==k):
    print('True')
else:
    print('False')
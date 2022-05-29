a=int(input())
sl=len(str(a))
k=a*1
sum=0
while a:
    r=a%10
    sum=sum+r**sl
    sl=sl-1
    a=a//10
if(sum==k):
    print('True')
else:
    print('False')
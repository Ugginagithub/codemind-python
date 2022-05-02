a=int(input())
k=a
sum=0
while a:
    r=a%10
    sum=sum+r
    a=a//10
if k%sum==0:
    print('True')
else:
    print('False')
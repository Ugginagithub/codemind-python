a=int(input())
rev=0
k=a*1
while a:
    r=a%10
    rev=rev*10+r
    a=a//10
if(rev==k):
    print('True')
else:
    print('False')
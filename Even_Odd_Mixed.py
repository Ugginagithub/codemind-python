n=int(input())
e=0
o=0
while n:
    if(n%10)%2==0:
        e+=1
    else:
        o+=1
    n//=10
if(e==0 and o>0):
    print('Odd')
elif(o==0 and e>0):
    print('Even')
else:
    print('Mixed')
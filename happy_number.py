n=int(input())
s=0
while(True):
    while(n!=0):
        s+=(n%10)**2
        n=n//10
    if(s==1 or s==7):
        print('True')
        break
    elif(s<10):
        print('False')
        break
    else:
        n=s
        s=0
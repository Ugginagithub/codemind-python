def sd(n):
    t=n
    c=0
    c1=0
    while(n):
        r=n%10
        c+=1
        if(r==0):
            break
        if(t%r==0):
            c1+=1
        n=n//10
    if(c==c1):
        return 1
    else:
        return 0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(sd(i)):
        print(i,end=' ')
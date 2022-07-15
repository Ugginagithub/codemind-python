def p(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
n=int(input())
c=0
c1=0
for i in range(1,n+1):
    if(n%i==0):
        if(p(i)):
            c+=1
        else:
            c1+=1
print(c1)

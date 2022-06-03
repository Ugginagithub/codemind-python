def p(n):
    if(n==1):
        return 1
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    else:
        return 1
a=int(input())
b=int(input())
k=a+b
for i in range(1,100000):
    if(p(k+i)):
        print(i)
        break
a,b=map(int,input().split())
c=0
for i in range(1,b+1):
    if i%2==0:
        c=c+1
    else:
        print(a,"x",i,"=",a*i)
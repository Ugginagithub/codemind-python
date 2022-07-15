n,m=map(int,input().split())
arr=list(map(int,input().split()))
c=0
c1=0
for i in arr:
    if i<0:
        if(len(str(i))-1==m):
            c+=1
    else:
        if(len(str(i))==m):
            c1+=1
print(c+c1)
n=int(input())
arr=list(map(int,input().split()))
b=[]
c=[]
for i in arr:
    if(i%2==0):
        b.append(i)
    else:
        c.append(i)
print(*b,end=' ')
print(*c,end=' ')
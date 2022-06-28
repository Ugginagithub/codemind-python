a,b=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
b=[]
c=[]
for i in arr1:
    for j in arr2:
        if(i==j):
            b.append(i)
for i in b:
    if i not in c:
        c.append(i)
print(*c)
n,m=map(int,input().split())
b=[]
e=0
o=0
for i in range(n):
    arr=list(map(int,input().split()))
    b.append(i)
    for i in arr:
        if(i%2==0):
            e+=i
        else:
            o+=i
print(e,o)
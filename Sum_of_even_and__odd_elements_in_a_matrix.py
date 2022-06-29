n,m=map(int,input().split())
b=[]
e=0
o=0
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
    for i in a:
        if i%2==0:
            e+=i
        else:
            o+=i
print(e,o)

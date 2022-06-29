n,m=map(int,input().split())
b=[]
s=0
for i in range(n):
    a=list(map(int,input().split()))
    b.append(a)
    for i in a:
        s+=i
print(s)
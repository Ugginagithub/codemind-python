n,m=map(int,input().split())
b=[]
s=0
for i in range(n):
    arr=list(map(int,input().split()))
    b.append(i)
    for i in arr:
        s+=i
print(s)
n=int(input())
arr=list(map(int,input().split()))
s=0
c=0
for i in arr:
    s+=i
k=s//n
for i in arr:
    if(i<=k):
        c+=1
print(c)
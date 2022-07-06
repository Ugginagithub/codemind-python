n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in arr:
    k=i*i
    b.append(k)
h=sorted(b)
print(*h)
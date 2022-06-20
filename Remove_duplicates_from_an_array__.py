n=int(input())
arr=list(map(int,input().split()))
t=[]
for i in arr:
    if i not in t:
        t.append(i)
print(*t)
n=int(input())
arr=list(map(int,input().split()))
b=[]
a=[]
c=0
for i in range(n):
    for j in range(i):
        if(arr[i]==arr[j]):
            b.append(arr[j])
for i in arr:
    if i not in b:
        c+=1
        a.append(i)
if(c==0):
    print("-1")
else:
    print(max(a))
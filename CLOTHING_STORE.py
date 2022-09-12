n=int(input())
arr=list(map(int,input().split()))
x=list(set(arr))
l=[]
c=0
for i in range(len(x)):
    for j in range(len(arr)):
        if x[i]==arr[j]:
            c+=1
    l.append(c//2)
    c=0
print(sum(l))
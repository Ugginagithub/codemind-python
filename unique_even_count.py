n=int(input())
arr=list(map(int,input().split()))
b=[]
s=0
for i in arr:
    if i not in b:
        b.append(i)
for i in b:
    if(i%2==0):
        s+=1
print(s)
n=int(input())
arr=list(map(int,input().split()))
s=''
b=[]
for i in arr:
    s+=str(i)
s1=int(s)+1
for i in str(s1):
    b.append(i)
print(*b)
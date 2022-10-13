n=int(input())
a=list(map(int,input().split()))
s=0
for i in set(a):
    if i%2!=0:
        s+=1
print(s)
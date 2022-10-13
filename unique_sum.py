n=int(input())
a=list(map(int,input().split()))
s=0
for i in set(a):
    s+=i
print(s)
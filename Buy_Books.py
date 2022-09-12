n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=sum(a)
s1=sum(b)
if s-s1>0:
    print('0')
else:
    print(s1-s)
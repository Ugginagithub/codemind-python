def minind(a):
    m=a[0]
    for i in range(len(a)):
        if m>a[i]:
            m=a[i]
    return m
n=int(input())
a=list(map(int,input().split()))
m=a[0]
l=[]
while n>0:
    c=0
    m=minind(a)
    flag=0
    for i in range(len(a)):
        if a[i]-m>=0:
            c+=1
    for i in a:
        if i==m:
            flag+=1
    for i in range(flag):
        a.remove(m)
    print(c)
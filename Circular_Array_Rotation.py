x,y,z=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(z):
    n=int(input())
    l.append(n)
for i in range(y):
    temp=a[0]
    a[0]=a[x-1]
    for j in range(1,x):
        p=a[j]
        a[j]=temp
        temp=p
for i in l:
    print(a[i])
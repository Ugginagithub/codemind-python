n,x=map(int,input().split())
a=list(map(int,input().split()))
sc=0
sk=0
for i in a:
    if sk>1:
        break
    if i>x:
        sk+=1
    else:
        sc+=1
print(sc)
def factsum(n):
    s=1
    for i in range(2,n+1):
        if n%i==0:
            s+=i
    return s
a=input()
a=a.split(",")
res=[]
for i in a:
    b=factsum(int(i))
    if str(b) in a:
        res.append(int(i))
if(len(res)==0):
   print("-1")
else:
    print(*sorted(res))
    
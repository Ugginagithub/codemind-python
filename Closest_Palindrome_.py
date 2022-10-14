def pal(n):
    rev=0
    temp=n
    while n:
        rev=rev*10+n%10
        n=n//10
    if rev==temp:
        return 1
    return 0
n=int(input())
for i in range(n-1,1,-1):
    if pal(i):
        p=i
        break
temp=n+1
while temp!=0:
    if pal(temp):
        q=temp
        break
    temp+=1
if (n-p)<(q-n):
    print(p)
elif(n-p)==(q-n):
    print(p,q,end=' ')
else:
    print(q)
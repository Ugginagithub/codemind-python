def dig(n):
    c=0
    while n:
        r=n%10
        c+=1
        n=n//10
    if c%2==0:
        return(True)
    else:
        return(False)
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if(dig(arr[i])):
        c+=1
print(c)
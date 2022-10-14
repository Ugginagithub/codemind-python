a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    s=0
    c=0
    while temp!=0:
        j=temp%10
        if j!=0:
            if i%j==0:
                c+=1
        s+=1
        temp=temp//10
    if c==s:
        print(i,end=' ')
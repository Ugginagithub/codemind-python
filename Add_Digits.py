a=int(input())
while a>9:
    s=0
    while a>0:
        r=a%10
        s=s+r
        a=a//10
    a=s
print(s)
def lcm(a,b):
    if a>b:
        big=a
    else:
        big=b
    while(True):
        if (big%a==0) and (big%b==0):
            lcm=big
            break
        big+=1
    return lcm
a,b=map(int,input().split())
print(lcm(a,b))
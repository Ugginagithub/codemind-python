def fact(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a
n=int(input())
for i in range(1,n+1):
    b=int(input())
    print(fact(b))
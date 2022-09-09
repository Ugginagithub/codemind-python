n=int(input())
for i in range(n):
    a=int(input())
    s=0
    arr=list(map(int,input().split()))
    for i in arr:
        s+=i
    m=a*(a+1)//2
    print(abs(m-s))
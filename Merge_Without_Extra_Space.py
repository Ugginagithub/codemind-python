for _ in range(int(input())):
    m,n=map(int,input().split())
    arr=list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    c=[]
    for i in arr:
        c.append(i)
    for i in arr1:
        c.append(i)
    print(*sorted(c))
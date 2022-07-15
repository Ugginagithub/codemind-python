n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    if i<0:
        print(len(str(i))-1,end=' ')
    else:
        print(len(str(i)),end=' ')
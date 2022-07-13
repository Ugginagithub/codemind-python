n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+1):
        if(i>=j):
            print(chr(64+i),end=' ')
        else:
            print('',end='')
    print()
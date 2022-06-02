n=int(input())
for i in range(1,n+1):
    k=input()
    c=0
    for j in k:
        if j in '0123456789':
            c+=1
    if c==0:
        print('No')
    else:
        print('Yes')
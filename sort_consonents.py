s=input().split(' ')
l=[]
v='AEIOUaeiou'
for i in s:
    for j in i:
        if j not in v:
            l.append(j)
    l.sort()
    k=0
    for j in i:
        if j in v:
            print(j,end='')
        else:
            print(l[k],end='')
            k+=1
    print(end=' ')
    l.clear()
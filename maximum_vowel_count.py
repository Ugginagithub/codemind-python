x=list(map(str,input().split()))
c=0
d=[]
for i in x:
    for j in i:
        if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
            c+=1
        elif j=='A' or j=='E' or j=='I' or j=='O' or j=='U':
            c+=1
    d.append(c)
    c=0
print(max(d))
x=input()
d=[]
for i in x:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        d.append(i)
    elif  i=='A' or i=='I' or i=='O' or i=='U' or i=='E':
        d.append(i)
d=sorted(set(d),key=d.index)
if d!=[]:
    print(*d)
else:
    print('-1')
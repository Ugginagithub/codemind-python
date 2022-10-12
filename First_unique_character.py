x=input()
c=0
for i in x:
    if i>='a' and i<='z':
        if x.count(i)==1:
            print(i,end="")
            c+=1
            break
if c==0:
    print('-1')
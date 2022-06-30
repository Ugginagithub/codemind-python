n=input()
a=0
a1=0
for i in n:
    if i=='z':
        a+=1
    if i=='o':
        a1+=0.5
if(a==a1):
    print("Yes")
else:
    print("No")
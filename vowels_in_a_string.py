n=input()
n=list(n)
k=input()
z=0
for i in range(len(n)):
    if n[i]==k:
        x=i
        z=1
        break
if z==0:
    print("False")
else:
    print(True)
    print(x)
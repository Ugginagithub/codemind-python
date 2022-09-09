m=int(input())
n=int(input())
a=[]
s=0
for x in range(m):
    a.append([int(y) for y in input().split()])
for i in a:
    for j in i:
        s+=j
print(s)
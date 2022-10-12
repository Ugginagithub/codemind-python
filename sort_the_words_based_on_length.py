s=input().split()
l=[]
sum=0
for i in s:
    for j in i:
        sum+=ord(j)
    l.append([sum,i])
    sum=0
l.sort()
for i in l:
    print(i[1],end=' ')
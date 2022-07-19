n=int(input())
arr=list(map(int,input().split()))
e=[]
o=[]
for i in arr:
    if(i%2==0):
        e.append(i)
    else:
        o.append(i)
i=0
j=0
while i<len(e) or j<len(o):
    if j<len(o):
        print(o[j],end=' ')
        j+=1
    if(i<len(e)):
        print(e[i],end=' ')
        i+=1
if n%2!=0:
    print('0')
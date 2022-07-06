n=int(input())
arr=list(map(int,input().split()))
se=0
so=0
for i in range(n):
    if(i%2==0):
        se+=arr[i]
    else:
        so+=arr[i]
k=abs(se-so)
if(k%4==0):
    print("X")
else:
    print("Y")
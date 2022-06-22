n=int(input())
arr=list(map(int,input().split()))
k=int(input())
sum=0
for i in arr:
    if(i==k):
        break
    sum=sum+i
print(sum+k) 
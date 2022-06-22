def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
n=int(input())
arr=list(map(int,input().split()))
lcm=1
for i in arr:
    lcm=lcm*i//gcd(lcm,i)
print(lcm)
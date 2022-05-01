num=int(input())
rev=0
while(num):
    r=num%10;
    rev=rev*10+r;
    num=num//10;
print(rev)
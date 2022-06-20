def sqr(n):
    c=n*n
    return c
def rev(a):
    s=0
    while a:
        r=a%10
        s=s*10+r
        a//=10
    return s
n=int(input())
n1=rev(n)
n2=rev(sqr(n1))
n3=sqr(n)
if(n2==n3):
    print('True')
else:
    print('False')
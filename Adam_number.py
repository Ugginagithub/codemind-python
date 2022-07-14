def sq(n):
    m=n*n
    return m
def rev(n):
    t=n
    rev=0
    while(n):
        rev=rev*10+n%10
        n=n//10
    return rev
n=int(input())
m=sq(n)
o=rev(n)
p=sq(o)
q=rev(p)
if(m==q):
    print('True')
else:
    print('False')
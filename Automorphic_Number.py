n=int(input())
l=len(str(n))
s=n**2
a=s%pow(10,l)
if(a==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
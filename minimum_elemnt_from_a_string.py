s=input()
s=s.split(' ')
n=len(s)
s=s[n-1]
n=min(s)
m=n.lower()
if s.count(m)!=0:
    print(m)
else:
    print(n)
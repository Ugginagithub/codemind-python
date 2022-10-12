def happy_num(n):
    p=set()
    while n!=1 and n!=7:
        n=sum(int(i)**2 for i in str(n))
        if n in p:
            return 0
        p.add(n)
    return 1
n=int(input())
if happy_num(n):
    print("True")
else:
    print("False")
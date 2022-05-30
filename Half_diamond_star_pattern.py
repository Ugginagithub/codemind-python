a=int(input())
if(a>=3):
    for i in range(0,a):
        for j in range(0,i+1):
            print('*',end='')
        print()
    for i in range(1,a):
        for j in range(0,a-i):
            print('*',end='')
        print()
else:
    print('The pattern is not possible')

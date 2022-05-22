n=int(input())
for i in range(1,n+1):
    b=int(input())
    c=0
    for j in range(1,b):
        if(j*j==b):
            c+=1
    if(c==0):
        print("False")
    else:
        print("True")
    
            
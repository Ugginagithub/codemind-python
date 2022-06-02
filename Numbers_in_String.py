a=input()
sum=0
for i in a:
    if i in '0123456789':
        sum+=int(i)
print(sum)
a=input()
cv=0
cc=0
cd=0
cs=0
for i in a:
    if i in 'aeiouAEIOU':
        cv+=1
    elif i in '1234567890':
        cd+=1
    elif i in ' ':
        cs+=1
    else:
        cc+=1
print("Vowels: %d"%cv)
print("Consonants: %d"%cc)
print("Digits: %d"%cd)
print("White spaces: %d"%cs)

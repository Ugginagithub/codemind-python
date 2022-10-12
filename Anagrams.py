def anagrams(s):
    a=[]
    for ch in s.lower():
        a.append(ch)
    d={}
    for ch in a:
        if ch not in d:
            d[ch]=1
        else:
            d[ch]=d[ch]+1
    return d
s1=input()
s2=input()
a=anagrams(s1)
b=anagrams(s2)
if a==b:
    print('True')
else:
    print("False")
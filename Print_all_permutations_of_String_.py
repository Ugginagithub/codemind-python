def permute(s,answer):
    if(len(s)==0):
        print(answer)
        return 
    for i in range(len(s)):
        ch=s[i]
        left_substr=s[0:i]
        right_substr=s[i+1:]
        result=left_substr+right_substr
        permute(result,answer+ch)
answer=""
s=input()
permute(s,answer)
def roman(n):
    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sys=["I","lV","V","lX","X","XL","L","XC","C","CD","D","CM","M"]
    i=12
    while n:
        r=n//num[i]
        n%=num[i]
        while r:
            print(sys[i],end="")
            r-=1
        i-=1
if __name__=="__main__":
    n=int(input())
    roman(n)
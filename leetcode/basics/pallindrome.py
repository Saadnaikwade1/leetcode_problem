# part 7 check if the given Number is Pallindrome or NOt
def ispal(n):
    num=n
    result=d=0
    while num>0:
        d=num%10
        result=result*10+d
        num//=10
    return result==n
print(ispal(2342))
# tc: O(log10(N)
# sc:O(1)

        
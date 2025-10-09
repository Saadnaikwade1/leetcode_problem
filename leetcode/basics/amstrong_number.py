# amstrong number - if a number is equal to lenof power of individual digit of sum then it is amstrong 
# 153 = 1^3+5^3+3^3
#     = 1 + 125 + 27
#     = 153

n=int(input())
m=n
sum=0
pow=len(str(n))
while m!=0:
    sum=sum+((m%10)**pow)
    m=m//10
if n==sum:
    print("amstrong number")
else:
    print("no")


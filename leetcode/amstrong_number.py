# amstrong number - if a number is equal to cube of individual digit of sum then it is amstrong 
# 153 = 1^3+5^3+3^3
#     = 1 + 125 + 27
#     = 153

n=int(input())
m=n
sum=0
while m!=0:
    sum=sum+((m%10)**3)
    m=m//10
if n==sum:
    print("amstrong number")
else:
    print("no")


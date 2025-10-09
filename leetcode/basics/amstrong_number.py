# amstrong number - if a number is equal to lenof power of individual digit of sum then it is amstrong 
# 153 = 1^3+5^3+3^3
#     = 1 + 125 + 27
#     = 153

n=int(input())
m=n
total=0
power=len(str(n))
while m!=0:
    total=total+((m%10)**power)
    m=m//10
if n==total:
    print("amstrong number")
else:
    print("no")

# Time & Space Complexity
# Operation              	    Complexity
# Loop through digits	    O(d) (d = number of digits)
# Space used	            O(1) (constant, no extra storage)

# So:
# Time Complexity: O(log₁₀n) or O(d)
# Space Complexity: O(1)

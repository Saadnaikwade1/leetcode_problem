# # factor of given number
# n=int(input())
# result=[]
# for i in range(1,n+1):
#     if n%i==0:
#         result.append(i)
# print(result)

# # tc:O(N)
# # sc:(k) k would be total no of factors (k factors stores the result)

# # solution:2
# n=int(input())
# result=[]
# for i in range(1,n//2):
#     if n%i==0:
#         result.append(i)
# result.append(n)
# print(result)

# sc:O(N/2) ~ O(N)
# tc:O(k)

# solution:3(optimised one)
n=int(input())
result=[]
for i in range(1,int(n**0.5)+1):#O(N)
    if n%i==0:
        result.append(i)
        if n//i!=i:
            result.append(n//i)
result.sort() # O(NlogN)
print(result)

# tc:O(root(N))+O(nlogn)
# sc:O(k)
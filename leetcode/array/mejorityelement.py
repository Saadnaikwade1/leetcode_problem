class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=list(set(nums))
        ans=m=0
        for i in n:
            x= nums.count(i)
            if x>m:
                m=x
                ans=i
                
        
        return ans
    
    
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#         return candidate
    
# Great question 👌 Let’s walk through the Boyer–Moore Voting Algorithm step by step, using an example.

# The algorithm’s idea:

# We keep one candidate for majority and a count.

# If the current number is the same as candidate → increment count.

# Otherwise → decrement count.

# If count reaches 0 → pick new candidate.

# Because the majority element appears more than n/2 times, it will always survive this cancellation process.
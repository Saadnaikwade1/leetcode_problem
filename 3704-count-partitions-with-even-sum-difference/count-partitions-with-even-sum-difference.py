class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total=sum(nums)
        prefix=0
        count=0
        
        for i in range(len(nums)-1):
            prefix=+nums[i]
            suffix=total-prefix

            if abs(prefix-suffix)%2==0:
                count+=1
        return count
       
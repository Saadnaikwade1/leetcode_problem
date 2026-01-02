class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for i in range(n):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for k,v in freq.items():
            if v==(n//2):
                return k
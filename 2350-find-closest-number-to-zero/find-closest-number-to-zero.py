class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closenum=nums[0]
        for i in nums:
            if abs(i) < abs(closenum):
                closenum=i
        if closenum < 0 and abs(closenum) in nums:
            return abs(closenum)
        return closenum
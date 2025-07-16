class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in d:
                return [d[diff],i]
            d[num]=i